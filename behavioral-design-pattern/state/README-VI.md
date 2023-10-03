## Source

https://refactoring.guru/design-patterns/state

## Cốt lõi:

> State là một mẫu thiết kế hành vi cho phép một đối tượng thay đổi hành vi của nó khi trạng thái nội bộ của nó thay
> đổi. Nó xuất hiện như là nếu đối tượng đã thay đổi lớp của nó.

## Structure

![alt tag](state.png)

Các bước tạo state chính:

1. Xác định các trạng thái (States):

- Xác định các trạng thái khác nhau mà đối tượng của bạn có thể tồn tại. Mỗi trạng thái sẽ được biểu diễn bằng một lớp
  đặc biệt.

2. Tạo các lớp trạng thái (State Classes):

- Đối với mỗi trạng thái được xác định ở bước 1, tạo một lớp đại diện cho trạng thái đó. Lớp này sẽ chứa hành vi cụ thể
  cho trạng thái đó.

3. Xác định và triển khai hành vi chung (Context):

- Tạo một lớp chứa trạng thái hiện tại và các phương thức để thay đổi trạng thái. Lớp này thường được gọi là "Context"
  và có một biến thành viên để lưu trạng thái hiện tại, cùng với các phương thức để thay đổi trạng thái và gọi hành vi
  tương ứng.

4. Kết nối Context với các State:

- Trong lớp Context, bạn cần thêm các phương thức để thiết lập và thay đổi trạng thái hiện tại, và sau đó gọi hành vi
  tương ứng từ lớp trạng thái hiện tại.

5. Sử dụng Mẫu State:

- Bây giờ bạn có thể sử dụng Mẫu State trong ứng dụng của mình bằng cách tạo đối tượng Context và gọi các phương thức
  của nó để thay đổi và kiểm soát trạng thái.

6. Thêm mới và mở rộng:

- Nếu bạn cần thêm trạng thái mới hoặc mở rộng hành vi của đối tượng, bạn chỉ cần tạo thêm lớp trạng thái mới và thêm
  các phương thức tương ứng vào lớp Context mà không cần sửa đổi mã hiện tại.

7. Kiểm tra và bảo trì:
   Đảm bảo kiểm tra kỹ lưỡng để đảm bảo rằng các trạng thái và hành vi hoạt động đúng. Bảo trì mã của bạn để đảm bảo
   tính nhất quán và hiệu quả của Mẫu State.

## Description

### Mục đích

Mục đích chính của mẫu thiết kế State (State Design Pattern) là cho phép bạn quản lý và thay đổi hành vi của một đối
tượng khi trạng thái của nó thay đổi. Mẫu thiết kế này giải quyết một số vấn đề quan trọng trong phát triển phần mềm,
bao gồm:

1. **Quản lý trạng thái:** Một đối tượng thường có nhiều trạng thái khác nhau và hành vi của nó phụ thuộc vào trạng thái
   hiện tại. Mẫu State giúp bạn quản lý các trạng thái này một cách dễ dàng và mô tả chúng dưới dạng các lớp độc lập.
2. **Loại bỏ sự phụ thuộc:** Bằng cách biểu diễn mỗi trạng thái như một đối tượng riêng biệt, mẫu State giúp loại bỏ sự
   phụ thuộc giữa trạng thái và hành vi của đối tượng. Điều này làm cho mã dễ đọc hơn và dễ bảo trì hơn.
3. **Thêm mới và mở rộng trạng thái và hành vi:** Mẫu State cho phép bạn thêm mới các trạng thái và hành vi một cách dễ
   dàng bằng cách tạo các lớp con mới cho mỗi trạng thái. Điều này giúp bạn mở rộng đối tượng mà không cần sửa đổi mã
   hiện tại.
4. **Giảm sự phức tạp:** Bằng cách chia nhỏ đối tượng thành các phần nhỏ hơn (các trạng thái), mẫu State giúp giảm sự
   phức tạp của đối tượng gốc và làm cho mã dễ quản lý hơn.
5. **Tạo ra mã linh hoạt và tái sử dụng:** Mẫu State tạo ra mã linh hoạt, cho phép bạn sử dụng lại các trạng thái và
   hành vi trong các đối tượng khác. Điều này giúp giảm lặp lại mã và tăng khả năng tái sử dụng.

## Khi nào thì sử dụng state

Design pattern "State" (còn gọi là "State Design Pattern") được sử dụng khi bạn muốn thay đổi hành vi của một đối tượng
khi trạng thái của nó thay đổi. Đây là một mẫu thiết kế thuộc loại hành vi (behavioral design pattern) và thường được sử
dụng trong các tình huống sau:

1. Khi bạn có một đối tượng có nhiều trạng thái và hành vi khác nhau tùy thuộc vào trạng thái đó. Sử dụng mẫu thiết kế
   State giúp bạn quản lý các trạng thái này một cách dễ dàng hơn.
2. Khi bạn muốn tránh sự phụ thuộc giữa trạng thái và hành vi của một đối tượng. Mẫu State cho phép bạn biểu diễn mỗi
   trạng thái như một đối tượng riêng biệt, giúp loại bỏ sự phụ thuộc và tạo ra một cấu trúc linh hoạt hơn.
3. Khi bạn muốn thêm hoặc thay đổi các trạng thái và hành vi của đối tượng mà không ảnh hưởng đến mã hiện tại. Mẫu State
   cho phép bạn thêm mới các trạng thái và hành vi một cách dễ dàng bằng cách tạo các lớp con mới.
4. Khi bạn muốn giảm sự phức tạp của đối tượng bằng cách chia nhỏ nó thành các phần nhỏ hơn có thể quản lý riêng biệt.
   Mẫu State giúp bạn tạo ra các lớp con riêng biệt cho từng trạng thái, từ đó giảm sự phức tạp của đối tượng gốc.

## Running

```
python main.py
python example.py
```