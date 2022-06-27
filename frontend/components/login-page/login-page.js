import React, { Component, useState } from "react";
import { TextInput, View } from "react-native";
import styles from './login-page-styles';


export default class LoginPage extends Component {
    render() {
        return (
            <View style={styles.container}>
                <TextInput
                style={styles.textInput}
                placeholder='USERNAME'
                />
                <TextInput
                style={styles.textInput}
                placeholder='USERNAME'
                />
            </View>
        );
    }

}
