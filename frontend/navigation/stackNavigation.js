import React from 'react';
import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import EventTest from '../test-pages/EventTest';
import EventPageTest from '../test-pages/EventPageTest';


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

