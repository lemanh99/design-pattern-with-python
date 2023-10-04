## Source

https://refactoring.guru/design-patterns/template-method

## Cốt lõi:

> Mẫu Template Method là một mẫu thiết kế hành vi, xác định khuôn khổ (skeleton) của một thuật toán trong lớp siêu (
> superclass) nhưng cho phép các lớp con ghi đè (override) các bước cụ thể của thuật toán mà không thay đổi cấu trúc của
> nó

## Structure

![alt tag](template-method.png)

Các bước tạo template method chính:

1. **Xác định quy trình hoặc thuật toán cơ bản:**

- Xác định quy trình hoặc thuật toán mà bạn muốn tạo thành một khung cơ bản (template). Xác định các bước cố định của
  quy trình này.

2. **Tạo lớp cơ sở (Abstract Class):**

- Tạo một lớp cơ sở (abstract class) hoặc giao diện (interface) để định nghĩa khung cơ bản cho quy trình hoặc thuật
  toán. Định nghĩa các phương thức trừu tượng (abstract methods) cho các bước cố định và định nghĩa một phương thức "
  template method" để gọi các bước này theo thứ tự cố định.

3. **Triển khai các lớp con (Concrete Classes):**

- Tạo các lớp con (concrete classes) kế thừa từ lớp cơ sở. Mỗi lớp con sẽ triển khai các phương thức trừu tượng để thực
  hiện các bước cố định của quy trình.

4. **Triển khai "template method":**

- Trong lớp cơ sở, triển khai phương thức "template method" bằng cách gọi các phương thức trừu tượng để thực hiện các
  bước cố định theo thứ tự đúng.

5. **Cho phép lớp con ghi đè:**

- Cho phép các lớp con ghi đè các phương thức trừu tượng để cung cấp triển khai cụ thể cho các bước trong quy trình hoặc
  để thêm vào hoặc thay đổi hành vi.

6. **Sử dụng Mẫu Template Method:**

- Sử dụng các lớp con để thực hiện các biến thể cụ thể của quy trình hoặc thuật toán. Bạn có thể gọi phương thức "
  template method" trên đối tượng của lớp con để thực hiện quy trình.

## Description

### Mục đích

Mục đích chính của Mẫu thiết kế Template Method (Template Method Design Pattern) là cho phép bạn xác định một khung cơ
bản (template) cho một quy trình hoặc thuật toán, trong đó các bước cụ thể của quy trình được triển khai trong các lớp
con. Dưới đây là các mục đích chính của Mẫu Template Method:

1. **Tạo một cấu trúc cố định cho quy trình hoặc thuật toán:** Mẫu Template Method giúp bạn xác định một cấu trúc tổng
   thể cho một quy trình hoặc thuật toán, trong đó các bước cố định đã được định sẵn trong lớp cơ sở. Điều này giúp duy
   trì tính nhất quán của quy trình.
2. **Tách biệt mã chung và mã cụ thể:** Mẫu Template Method cho phép bạn di chuyển mã chung và các bước cố định của quy
   trình vào lớp cơ sở, giảm trùng lặp mã và làm cho mã dễ bảo trì hơn.
3. **Cho phép mở rộng và tùy chỉnh:** Lớp con có thể ghi đè các phần cụ thể của quy trình nếu cần thiết, mà không ảnh
   hưởng đến cấu trúc tổng thể. Điều này cho phép bạn mở rộng và tùy chỉnh hành vi của các lớp con một cách linh hoạt.
4. **Xác định các điểm kết nối (hook points):** Bạn có thể định nghĩa các điểm kết nối (hook methods) trong quy trình,
   mà các lớp con có thể sử dụng để thêm vào hoặc thay đổi hành vi của quy trình.
5. **Áp dụng nguyên tắc Inversion of Control (IoC):** Mẫu Template Method là một ví dụ của nguyên tắc IoC, trong đó lớp
   cơ sở định nghĩa khung cơ bản và cho phép lớp con điều khiển thực hiện các phần cụ thể.
6. **Bảo trì tính đa hình (polymorphism):** Mẫu Template Method sử dụng tính đa hình để cho phép các lớp con cung cấp
   các triển khai cụ thể của các bước trong quy trình. Điều này giúp tạo ra mã linh hoạt và dễ mở rộng.

## Khi nào thì sử dụng template method

1. Khi bạn muốn xác định một cấu trúc chung cho một loạt các lớp có các bước thực hiện tương tự: Mẫu Template Method cho
   phép bạn định nghĩa một bộ khung cơ bản (template) với các bước thực hiện cố định, trong khi các lớp con có thể triển
   khai các bước cụ thể theo cách riêng biệt.
2. Khi bạn muốn tránh việc lặp lại mã giữa các lớp tương tự: Mẫu Template Method giúp bạn di chuyển mã chung vào lớp cơ
   sở và chỉ tạo mã cụ thể trong các lớp con, do đó giảm sự trùng lặp và tạo ra mã dễ bảo trì hơn.
3. Khi bạn muốn cho phép các lớp con thay đổi một số bước cụ thể mà không ảnh hưởng đến cấu trúc tổng thể: Mẫu Template
   Method cho phép các lớp con ghi đè (override) các phần cụ thể của quy trình mà chúng muốn thay đổi, trong khi vẫn duy
   trì cấu trúc tổng thể không thay đổi.
4. Khi bạn muốn kiểm soát quy trình tổng thể của một thuật toán và đặt ra các điểm hook (hook methods) để cho phép các
   lớp con mở rộng hoặc tùy chỉnh hành vi: Mẫu Template Method cho phép bạn xác định các điểm "hook" trong quy trình, mà
   lớp con có thể sử dụng để mở rộng hoặc tùy chỉnh hành vi.
5. Khi bạn muốn có một kiến trúc chung cho việc triển khai các loại plugin hoặc phần mở rộng (extensions): Mẫu Template
   Method giúp bạn xây dựng một kiến trúc cho việc triển khai các phần mở rộng của một ứng dụng một cách dễ dàng và mở
   rộng.
6. Khi bạn muốn đảm bảo tính nhất quán của một quy trình và không muốn cho phép các lớp con thay đổi hoặc vi phạm cấu
   trúc của nó: Mẫu Template Method định nghĩa một quy trình cố định và đảm bảo rằng nó sẽ được tuân theo bởi các lớp
   con.

Ví dụ phổ biến của việc sử dụng Mẫu Template Method bao gồm triển khai các phương thức cho quy trình của các loại trò
chơi (ví dụ: trò chơi turn-based), các bước trong quy trình sản xuất (ví dụ: quy trình sản xuất sản phẩm), và các loại
thuật toán (ví dụ: thuật toán sắp xếp) trong phát triển phần mềm.

## Running

```
python main.py
python example.py
```