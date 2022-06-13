import React, { useEffect, useState, Component } from 'react';
import { Text, View } from 'react-native';
import styles from '../styles/testStyles';

export default class EventTest extends Component {
    constructor(props) {
        super(props)
        this.state = {
            event: this.props.navigation.state.params.event
        }
    }

    render() {
        return (
            <View style={styles.container}>
                <Text>{this.state.event.name}</Text>
                <Text>date: {this.state.event.date}</Text>
                <Text>description: {this.state.event.description}</Text>
                <Text>start time: {this.state.event.start_time}</Text>
                <Text>end time: {this.state.event.end_time}</Text>
            </View>
        );
    }

}