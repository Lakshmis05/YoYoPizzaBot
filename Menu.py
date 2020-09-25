from flask import Flask, request, jsonify
import Database as connect
import GenerateResponse as res
import Error as err

app= Flask(__name__)
@app.route("/fetch", methods=["get", "post"])
def fetch():
    conn = connect.ConnectMySql()
    print(f"Connection status : {conn}")

    if(conn is False):
        return err.ReturnConnectionError()
    else:
        try:
            cur = conn.cursor()
            print(f"Cursor object : {cur}")
            query = ("select * from veg")
            cur.execute(query)
            return res.GenerateResponse(cur,msg)
        except Exception as e:
            print(e)
            return err.ReturnFetchError()
        finally:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True,port=3000)
