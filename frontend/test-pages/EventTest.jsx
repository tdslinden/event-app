import React, { useEffect, useState, Component } from 'react';
import { Text, View, TouchableOpacity } from 'react-native';
import { getAllEventObjects } from '../services/EventServices';
import styles from '../styles/testStyles';

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
            <View style={styles.container}>
                {this.state.events.map((event) => (
                    <TouchableOpacity 
                        key={event.id.toString()}
                        onPress={() => this.props.navigation.navigate('EventPage',{event: event})}
                    >
                        <Text>
                        {event.name}
                        </Text>
                    </TouchableOpacity>

                ))}
            </View>
        );
    }

}
