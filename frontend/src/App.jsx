import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Face from './Face'


function App() {
  const [check, setCheck] = useState(false)

  return (
    <div >
       <div>
       <input id="check" type="checkbox" onChange={(e)=>setCheck(e.target.checked)} /> 
        <label for="check">Распознавание с камеры</label>
      </div>
       
        {check&& <Face/>}
     
    </div>
  )
}

export default App
