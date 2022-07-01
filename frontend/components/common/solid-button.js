import { View, Button, Text } from "react-native"
import { TouchableOpacity } from "react-native-gesture-handler";
import styles from "./solid-button-styles";

const SolidButton = (props) => {
    return (
        <View style={styles.container}>
            <TouchableOpacity style={styles.button} onPress={props.onPress}>
                <Text style={styles.text}>
                    {props.title}
                </Text>
            </TouchableOpacity>
        </View>
    )
}

export default SolidButton;