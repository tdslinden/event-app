import React, { useEffect, useState, Component } from 'react';
import { Text, View } from 'react-native';
import { getAllEventObjects } from '../services/GetEventDetails';

export default class EventTest extends Component {
    constructor(props) {
        super(props)
        this.state = {
            events: []
        }
    }

    componentDidMount() {
        getAllEventObjects()
            .then((res) => {
                console.log(res)
                this.setState({ events: res })
                // testing console.log
                this.state.events.map((eventObject) => {
                    console.log(eventObject.name)
                })
            }).catch((error) => {
                console.log("api call error");
                alert(error.message);
            })
    }

    render() {
        return (
            <View>
                {this.state.events.map(event => (
                    <Text>{event.name}</Text>
                ))}
            </View>
        );
    }

}
