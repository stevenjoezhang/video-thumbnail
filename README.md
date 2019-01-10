# Video Thumbnail

Creating video thumbnails, based on ffmpeg and python (support both python2 and 3).  
基于ffmpeg和python创建视频在不同时间的截图，并将它们合成一张缩略图。

## Requirements
ffmpeg and python is required. You can use `apt-get`, `yum` or `brew` to install them.

## Install
```bash
# Clone this repository
git clone https://github.com/stevenjoezhang/video-thumbnail.git
# Go into the repository
cd video-thumbnail
```

## Run
```bash
python run.py /path/to/example.mp4
```
or

```bash
bash run.sh /path/to/example.mp4
```

## Usage
You may edit the files yourself. For example, you can change the value of `width_i` in `image.py`.

## Credits
* [Mimi](https://zhangshuqiao.org) Developer of this project.

## License
Released under the GNU General Public License v3  
http://www.gnu.org/licenses/gpl-3.0.html

## Demo
![](sample.jpg)
