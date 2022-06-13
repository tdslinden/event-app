import React from 'react';
import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import EventTest from '../screens/EventTest';
import EventPageTest from '../screens/EventPageTest';


export default class StackNavigation extends React.Component {
  render() {
    return <StackContainer />;
  }
}

const EventNavigator = createStackNavigator({
  Events: {
    screen: EventTest
  },
  EventPage: {
    screen: EventPageTest
  }
},{
    initialRouteName: "Events"
});

const StackContainer = createAppContainer(EventNavigator);

