## The content and style images fed to the tensorflow pretrained hub model and starts training 
stylized_image = hub_model(
    tf.constant(content_img),
    tf.constant(style_img)
)[0]

## Outputs the stylized image
plt.imshow(stylized_image[0])
plt.axis('off')
