# dog_sprite
Brownian motion for using sprite sheets with classes
![sample gif](./img/result.gif)

## Global constants
```python
display_width = 640
display_height = 480
size = (display_width, display_height)

FPS = 30
frames = FPS // 12
```

to complie all the images using ffmpeg
```shell
ffmpeg -r 30 -f image2 -i .\Snaps\%04d.png result.avi
```

## Graphics Styling
### Analogous Colors - Reds and Greens
#### Reds
##### Base
```
(255, 87, 51)
(255, 189, 51)
(219, 255, 51)
```
### Greens
```
(117, 255, 51)
(51, 255, 87)
(51, 255, 189)
```
### Complement - Blue
```
(51, 219, 255)
```
### Complement Analogous
#### Blues
##### Base Complement
```
(51, 219, 255)
(51, 117, 255)
(87, 51, 255)
```
##### Purples to Pink
```
(189, 51, 255)
(255, 51, 219)
(255, 51, 117)
```
