import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Face from './Face'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
        <Face/>
     
    </>
  )
}

export default App
