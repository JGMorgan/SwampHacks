'use strict';
import React, { Component } from 'react';
import {
  AppRegistry,
  Dimensions,
  StyleSheet,
  Text,
  Vibration,
  TouchableHighlight,
  View
} from 'react-native';
import Camera from 'react-native-camera';

var pattern = [0, 500, 200, 500];
class Veo extends Component {
  render() {
    return (
      <View style={styles.container}>
        <Camera
          captureTarget={Camera.constants.CaptureTarget.memory}
          ref={(cam) => {
            this.camera = cam;
          }}
          style={styles.preview}
          aspect={Camera.constants.Aspect.fill}>
          <Text style={styles.capture} onPress={this.takePicture.bind(this)}>[CAPTURE]</Text>
        </Camera>
      </View>
    );
  }

  takePicture() {
      this.camera.capture().then((data) => {
          console.log(data);
          /*app.models.predict(Clarifai.GENERAL_MODEL, {base64: data['data']}).then(
              function(response) {
                  console.log(response);
              },
              function(err) {
                  // there was an error
              }
          );*/
          return fetch('http://45.33.5.10:5000/', {
              method: 'POST',
              headers: {
                  'Accept': '*/*',
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  Image: data['data'],
              })
          })
      }).then((response) => {
          console.log(JSON.stringify(response).includes('"content-length":["4"]'));
          /*real hackathon code who coding*/
          if (JSON.stringify(response).includes('"content-length":["4"]')) {
              for (var i = 0; i < 5; i++) {
                  Vibration.vibrate(pattern);
              }
          }
      })
      .catch((error) => {console.log(error); return error});
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  preview: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    height: Dimensions.get('window').height,
    width: Dimensions.get('window').width
  },
  capture: {
    flex: 0,
    backgroundColor: '#fff',
    borderRadius: 5,
    color: '#000',
    padding: 10,
    margin: 40
  }
});


AppRegistry.registerComponent('Veo', () => Veo);
