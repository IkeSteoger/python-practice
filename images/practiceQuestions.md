# Practice Questions

### 1. What is an RGBA value?

- an extension of RGB color values with an alpha channel - which specifies the opacity for a color

### 2. How can you get the RGBA value of `'CornflowerBlue'` from the `Pillow` module?

- using `ImageColor.getcolor('CornflowerBlue', 'RGBA')`

### 3. What is a box tuple?

- it is a tuple value of four integers: left edge x-coordinate, the top edge y-coordinate, the width, and the height

### 4. What function returns an `Image` object for, say, an image file named `zophie.png`?

- `Image.open('zophie.png')`

### 5. How can you find out the width and height of an `Image` object’s image?

- `imageObj.size`

### 6. What method would you call to get `Image` object for a 100×100 image, excluding the lower-left quarter of it?

- `imageObj.crop((0, 50, 50, 50))`

### 7. After making changes to an `Image` object, how could you save it as an image file?

- `imageObj.save('newPictureName.png')`

### 8. What module contains Pillow’s shape-drawing code?

- `ImageDraw`

### 9. `Image` objects do not have drawing methods. What kind of object does? How do you get this kind of object?

- `ImageDraw` objects have methods such as `point()`, `line()`, or `rectangle()`. You get this object by passing the `Image` object to the `ImageDraw.Draw()` function.
