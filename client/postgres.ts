import { Pool, Client } from 'pg';

export class postgres {
    static getInstance: postgres

    pool: Pool
    client: Client

    constructor() {
        postgres.getInstance = this
    }

    async connect() {
        //this.client = await this.pool.connect()
        this.client = new Client()
        this.client.connect()
        const res = await this.client.query('SELECT NOW()')
    }

    async addMessageInHistory(client_name: string, chat_id: string, message_id: string, sender: string, content: string) {
        const global_message_id = client_name + '.' + chat_id + '.' + message_id
        const query = "INSERT INTO chat_history(client_name, chat_id, message_id, global_message_id, sender, content) VALUES($1, $2, $3, $4, $5, $6) RETURNING *"
        const values = [ client_name, chat_id, message_id, global_message_id, sender, content ]

        this.client.query(query, values, (err, res) => {
            if (err) {
              console.log(err.stack)
            } else {
              console.log(res.rows[0])
            }
          })
    }

    async getHistory(length: number, client_name: string, chat_id: string) {
        const query = "SELECT * FROM chat_history WHERE client_name=$1 AND chat_id=$2"
        const values = [ client_name, chat_id ]
        return await this.client.query(query, values, (err, res) => {
            const _res = []
            if (res !== undefined && res !== null && res.rows !== undefined) {
                console.log('length: ' + res.length)
                for(let i = 0; i < res.rows.length; i++) {
                    console.log(res.rows[i])
                    _res.push({ author: res.rows[i].sender, content: res.rows[i].content })

                    if (i >= length) break
                }
            }  
            return _res
        })
    }

    async deleteMessage(client_name: string, chat_id: string, message_id: string) {
        const query = "DELETE FROM chat_history WHERE client_name=$1 AND chat_id=$2 AND message_id=$3"
        const values = [ client_name, chat_id, message_id ]

        await this.client.query(query, values, (err, res) => {})
    }

    async updateMessage(client_name: string, chat_id: string, message_id: string, newContent: string) {
        const query = "UPDATE chat_history SET content=$1 WHERE client_name=$2 AND chat_id=$3 AND message_id=$4"
        const values = [ newContent, client_name, chat_id, message_id ]

        await this.client.query(query, values, (err, res) => {})
    }

    async messageExists(client_name: string, chat_id: string, message_id: string) {
        const query = "SELECT * FROM chat_history WHERE client_name=$1 AND chat_id=$2 AND message_id=$3"
        const values = [ client_name, chat_id, message_id ]

        return await this.client.query(query, values, (err, res) => {
            return res !== undefined && res !== null && res.rows !== undefined && res.rows.length > 0
        })
    }

    async getNewMessageId(client_name: string, chat_id: string) {
        const query = "SELEC * FROM chat_history WHERE client_name=$1 AND chat_id=$2"
        const values = [ client_name, chat_id ]

        return await this.client.query(query, values, (err, res) => {
            if (res !== undefined && res !== null && res.rows !== undefined) {
                return res.length + 1
            } else {
                return 1
            }
        })
    }
}