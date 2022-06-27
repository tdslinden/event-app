import StackNavigation from './navigation/stackNavigation';
import React from 'react';
import SolidButton from './components/common/solid-button';



export default class App extends React.Component {
  render() {
    return <SolidButton title="hello there" onPress={() => console.log("pressed")}/>;
  }
}



