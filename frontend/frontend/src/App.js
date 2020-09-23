import React, { useState, useEffect } from "react"
import "./App.css"

const loginAndGetItems = async () => {
  const tokenRequestPayload = new URLSearchParams()
  tokenRequestPayload.append("username", "admin@frontend.com")
  tokenRequestPayload.append("password", "changethis")

  const tokenResponse = await fetch("/api/v1/login/access-token", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: tokenRequestPayload,
  })
  const { access_token: token } = await tokenResponse.json()

  const itemsResponse = await fetch("/api/v1/items/", {
    // careful, you need the trailing slash ;)
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })
  return itemsResponse.json()
}

const App = () => {
  const [data, setData] = useState({ items: [] })

  useEffect(() => {
    const getData = async () => {
      const items = await loginAndGetItems()
      setData({ items })
    }
    getData()
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <pre style={{ textAlign: "left" }}>
          Items: {JSON.stringify(data.items, null, 2)}
        </pre>
      </header>
    </div>
  )
}

export default App
