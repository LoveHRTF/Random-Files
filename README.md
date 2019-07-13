# Random-Files
This program randomly select and show a file under specificed directory.

## Usage

* Show one random image

```
$python run.py --path=PATH
```

* Show five random images

```
$python run.py --path=PATH --iters=5
```

* Show five random images with interval of 0.1 seconds

```
$python run.py --path=PATH --iters=5 --interval=0.1
```

* Show five random PNG images

```
$python run.py --path=PATH --iters=5 --interval=0.1 --tpye=PNG
```

* Open by using system default application for images
```
$python run.py --path=PATH --type=IMG --sysImgApp=1
```

* Open random video file
```
$python run.py --path=PATH --type=Video
```

* Open any random file
```
$python run.py --path=PATH --type=Any --sysImgApp=1
```


## TODO
* Add randomly delete specific type of file feature


