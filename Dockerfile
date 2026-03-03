# -----------------------------------------------------------------------------
# ■ BUild Image
# -----------------------------------------------------------------------------
#　Please execute the following command in the project root directory
#
#   docker build -t star-office-ui .
#
# -----------------------------------------------------------------------------
# ■ Run Container
# -----------------------------------------------------------------------------
# To run a container from the built image,
# please execute the following command:
#
#   docker run -p 18791:18791 --name star-office-ui  -v $(pwd):/app  star-office-ui
#
# -----------------------------------------------------------------------------
# ■ How to access
# -----------------------------------------------------------------------------
# After startup, access the following URL
#
#   http://localhost:18791
#
# -----------------------------------------------------------------------------


FROM python:3.12-slim

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/backend

CMD ["python3", "app.py"]