# Confetti Spaghetti

Thanks to www.bensound.com for the great generic music. Couldn't have done this without you Benjamin.

## Usage (Debian-based systems)

1. Clone this repository
```shell
git clone https://github.com/ksteensig/confettispaghetti
```

2. Install pip3, ImageMagick and FFmpeg
```shell
sudo apt-get install python3-pip imagemagick ffmpeg
```

3. Install following Python3 packages
```shell
sudo pip3 install praw imgurpython gTTS moviepy
```

4. Make a change to the file `/etc/ImageMagick-6/policy.xml` from this
```xml
<policymap>
  <policy domain="cache" name="shared-secret" value="passphrase"/>
  <policy domain="coder" rights="none" pattern="EPHEMERAL" />
  <policy domain="coder" rights="none" pattern="URL" />
  <policy domain="coder" rights="none" pattern="HTTPS" />
  <policy domain="coder" rights="none" pattern="MVG" />
  <policy domain="coder" rights="none" pattern="MSL" />
  <policy domain="coder" rights="none" pattern="TEXT" />
  <policy domain="coder" rights="none" pattern="SHOW" />
  <policy domain="coder" rights="none" pattern="WIN" />
  <policy domain="coder" rights="none" pattern="PLT" />
  <policy domain="path" rights="none" pattern="@*" />
</policymap>
```
To this
```xml
<policymap>
  <policy domain="cache" name="shared-secret" value="passphrase"/>
  <policy domain="coder" rights="none" pattern="EPHEMERAL" />
  <policy domain="coder" rights="none" pattern="URL" />
  <policy domain="coder" rights="none" pattern="HTTPS" />
  <policy domain="coder" rights="none" pattern="MVG" />
  <policy domain="coder" rights="none" pattern="MSL" />
  <policy domain="coder" rights="none" pattern="TEXT" />
  <policy domain="coder" rights="none" pattern="SHOW" />
  <policy domain="coder" rights="none" pattern="WIN" />
  <policy domain="coder" rights="none" pattern="PLT" />
  <!--policy domain="path" rights="none" pattern="@*" /-->
</policymap>
```

5. Now copy `keys.py.template` to `keys.py`
```shell
cp keys.py.template keys.py
```

6. Insert your reddit and imgur developer API credentials in the `keys.py`

7. Run the program and enter the name of a subreddit which contains videos hosted by reddit or imgur
```python
python3 main.py
```

8. Be patient and wait for the video to finish, the video will be named output.mp4 and put into a folder named `$(subreddit)/$(timestamp)`


## Configuring

In `convert.py` there is a function called `convert`. This function has two parameters for adjusting time limits, `tduration` is the maximum overall video length and `mduration` is the minimum length of the individual clips.

You shouldn't change the defaults in `convert` itself, but you can set the parameters from where it's called in `main.py`. This should ideally be set in a config file which might be added at some point.
