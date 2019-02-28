## Speed up video

```bash
ffmpeg -i /Users/dth/Desktop/take11.m4v  -filter:v "setpts=0.5*PTS" /Users/dth/Desktop/take11_fast.m4v
```
