import React, { useState } from 'react'

function App() {
  const [phrase, setPhrase] = useState([]) // Phrase after backend processing
  const [name,setName] = useState(null) // Name from first input box
  const [zip,setZip] = useState(null) // Zip code from second input box
  const [print,setPrint] = useState(false) // Print status

  // Sets the name of the user and the print status to false, in case of consecutive usage
  function getName(val)
  {
    console.warn(val.target.value)
    setName(val.target.value)
    setPrint(false)
  }

  // Sets the zip of the user and the print status to false, in case of consecutive usage
  function getZip(val)
  {
    console.warn(val.target.value)
    setZip(val.target.value)
    setPrint(false)
  }

  // Sends the data as a JSON Object to the Flask backend for processing 
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
    // Routes to /create_phrase endpoint in ../backend/server.py
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