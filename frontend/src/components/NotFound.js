import NoResults from '../assets/no-results.png'
import React from 'react'
import Asset from './Asset'

const NotFound = () => {
  return (
    <Asset
    src= {NoResults}
    message= "Sorry, the page you're looking for doesn't exist"
    />
  )
}

export default NotFound