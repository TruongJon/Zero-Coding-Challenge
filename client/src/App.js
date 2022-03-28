import React, { useState } from 'react'

function App() {
  const [phrase, setPhrase] = useState([])
  const [name,setName] = useState(null)
  const [zip,setZip] = useState(null)
  const [print,setPrint] = useState(false)

  function getName(val)
  {
    console.warn(val.target.value)
    setName(val.target.value)
    setPrint(false)
  }

  function getZip(val)
  {
    console.warn(val.target.value)
    setZip(val.target.value)
    setPrint(false)
  }

  function processData()
  {
    const userData = {
      name : name,
      zip : zip
    }
    console.log(JSON.stringify(userData));
    const request = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    };
    fetch('/create_phrase', request).then(response => 
      response.json().then(data => {
        console.log(response)
        setPhrase(data)
        setPrint(true)
      })
    )
  }

  return (
    <div className="app" style={{display: 'flex', flexDirection: 'column',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
    {
      print?
      <h1>{phrase.output}</h1>
      :null
    }
    
    <div>
    <label> First / Last Name </label>
    <input type="text" onChange={getName} />  
    </div>
    <div>
    <label> Postal Code (US) </label>
    <input type="text" onChange={getZip} />
    </div>

    <button onClick={()=>processData()}> Process Data </button>
    </div>
  );
}

export default App