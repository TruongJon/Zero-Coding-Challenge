import React, { useState } from 'react'

function App() {
  
  const [name,setName]=useState(null)
  const [zip,setZip]=useState(null)
  const [print,setPrint]=useState(false)

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

  return (
    <div className="app" style={{display: 'flex', flexDirection: 'column',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
    {
      print?
      <h1>{name} {zip} is in x county and has a population of y</h1>
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

    <button onClick={()=>setPrint(true)}> Process Data </button>
    </div>
  );

}
export default App