def load_image(img_path):
  
    img = tf.io.read_file(img_path) ## Reading the image with tensorflow 
  
    img = tf.image.decode_image(img, channels=3) ## Decoding the image for no. of channels and converting into 3 channels 
  
    img = tf.image.resize(img, (256, 256)) ## Resizing the image for feeding to VGG model
  
    img = tf.cast(img, tf.float32) / 255.0 ## Normalisation for better inference to model 
  
    img = tf.expand_dims(img, axis=0) ## Expanding the dimension from (512,512,3) to (1,512,512,3)
  
  return img
