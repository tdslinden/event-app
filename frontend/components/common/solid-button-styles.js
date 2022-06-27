import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
      display: 'flex',
      flexDirection: 'column'
    },
    button: {
        borderRadius: 10,
        borderWidth: 1,
        borderColor: 'blue',
        height: 50,
        width: 350,
        margin: 15,
        textAlign: 'center',
        alignItems: 'center',
        justifyContent: 'center',
        display: 'flex',
        backgroundColor: 'blue'
    },
    text: {
        fontSize: 20,
        color: 'white'
    }
  });
  
  export default styles;