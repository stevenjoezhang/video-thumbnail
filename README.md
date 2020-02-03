# Video Thumbnail

基于 ffmpeg 和 Python3 创建视频在不同时间的截图，并将它们合成一张缩略图。  
Creating video thumbnails, based on ffmpeg and Python (support Python3 only).

## Requirements

Python3 and ffmpeg is required. You can use `apt`, `yum` or `brew` to install them.

## Install

```bash
# Clone this repository
git clone https://github.com/stevenjoezhang/video-thumbnail.git
# Go into the repository
cd video-thumbnail
```

## Usage

```bash
python3 run.py /path/to/example.mp4
```
or

```bash
bash run.sh /path/to/example.mp4
```

You may edit the files yourself. For example, you can change the value of `width_i` in `image.py`.

## Credits

* [Mimi](https://zhangshuqiao.org) Developer of this project.

## License

Released under the GNU General Public License v3  
http://www.gnu.org/licenses/gpl-3.0.html

## Todo

Use https://github.com/kkroening/ffmpeg-python

## Demo

![](sample.jpg)
