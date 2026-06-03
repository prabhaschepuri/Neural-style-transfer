style_img = load_image(r'style_img_path')
content_img = load_image(r'content_img_path')

## prints min and max value of the image activations with range [0,1]
print(tf.reduce_min(content_img))
print(tf.reduce_max(content_img))

print(tf.reduce_min(style_img))
print(tf.reduce_max(style_img))

# Prints the shape and data type of content and style images which is in 4D dimension
print("Content:", content_img.shape, content_img.dtype)
print("Style:", style_img.shape, style_img.dtype)
