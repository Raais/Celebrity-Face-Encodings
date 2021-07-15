This repository contains face encodings of 100 celebrities ready for use with [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)

## Usage

```python
numpy.loadtxt(filename)
```

## Example

```python
dir = os.path.dirname(__file__)
encdir = os.path.join(dir,'encodings')
imgdir = os.path.join(dir,'images')

img = face_recognition.load_image_file("test.jpg")
fenc = face_recognition.face_encodings(img)[0]

for file in os.listdir(encdir):
    denf = os.path.join(encdir,file)
    denc = np.loadtxt(denf)

    res = face_recognition.compare_faces(
        [denc], fenc)
    if res[0] == True:
        print("Matched: " + file)
        break
```
