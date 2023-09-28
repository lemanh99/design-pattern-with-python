## Source

https://refactoring.guru/design-patterns/mediator

## Cốt lõi:

> Mediator là một mẫu thiết kế hành vi cho phép bạn giảm thiểu sự phụ thuộc hỗn loạn giữa các đối tượng. Mẫu thiết kế
> này hạn chế việc truyền thông trực tiếp giữa các đối tượng và buộc chúng phải hợp tác chỉ thông qua một đối tượng trung
> gian

## Structure

![alt tag](mediator.png)

Các bước tạo mediator chính:

1. Xác định các thành phần cần giao tiếp

- Xác định các đối tượng hoặc thành phần trong hệ thống của bạn mà bạn muốn giảm sự phụ thuộc và thực hiện giao tiếp
  thông qua một mediator.

2. Định nghĩa interface Mediator

- Tạo một giao diện (interface) cho Mediator. Interface này sẽ định nghĩa các phương thức mà các đối tượng trong hệ
  thống có thể sử dụng để giao tiếp với nhau thông qua mediator.

3. Tạo lớp Mediator cụ thể

- Triển khai lớp Mediator cụ thể (concrete mediator) dựa trên interface Mediator. Lớp này sẽ chứa logic xử lý giao tiếp
  giữa các đối tượng.

4. Định nghĩa interface Colleague

- Tạo một giao diện (interface) cho các đối tượng (Colleague) trong hệ thống. Giao diện này sẽ định nghĩa các phương
  thức
  mà mediator có thể sử dụng để gửi thông điệp cho các đối tượng.

5. Triển khai các lớp Colleague

- Triển khai các lớp cụ thể của Colleague interface. Mỗi lớp này sẽ có một tham chiếu đến Mediator để gửi và nhận thông
  điệp.

6. Kết nối các đối tượng với Mediator

- Trong ứng dụng thực tế, bạn sẽ tạo các đối tượng của Mediator, Colleague, và sau đó kết nối chúng lại với nhau.

## Description

### Mục đích

Mục đích chính của việc sử dụng Mediator design pattern là giảm sự phụ thuộc và tạo ra một cơ chế giao tiếp linh hoạt
giữa các đối tượng trong một hệ thống phức tạp. Dưới đây là các mục đích cụ thể khi sử dụng Mediator pattern:

1. **Giảm sự phụ thuộc:** Mediator pattern giúp giảm sự phụ thuộc giữa các đối tượng trong hệ thống. Thay vì các đối
   tượng tương tác trực tiếp với nhau, chúng tương tác thông qua một mediator. Điều này làm cho các đối tượng độc lập
   hơn và dễ dàng bảo trì.
2. **Tạo sự linh hoạt:** Mediator pattern tạo sự linh hoạt trong hệ thống bằng cách cho phép thêm mới các đối tượng hoặc
   thay đổi cách chúng tương tác mà không cần sửa đổi nhiều mã nguồn. Bạn chỉ cần thay đổi mediator hoặc thêm một đối
   tượng mới và kết nối nó với mediator.
3. **Giảm sự rắc rối:** Khi mối quan hệ giữa các đối tượng trở nên phức tạp và khó quản lý, Mediator pattern giúp giảm
   sự rắc rối bằng cách chuyển trách nhiệm quản lý tương tác vào một điểm trung tâm.
4. **Tăng khả năng mở rộng:** Pattern này giúp dễ dàng mở rộng hệ thống bằng cách thêm các đối tượng mới và chỉ cần cập
   nhật mediator để xử lý tương tác của chúng.
5. **Tạo sự trừu tượng:** Mediator pattern tạo ra một lớp trung gian trừu tượng, làm cho giao tiếp giữa các đối tượng
   trở nên hiệu quả và dễ hiểu hơn.
6. **Mô phỏng giao tiếp không biết về nhau:** Mediator pattern thường được sử dụng để mô phỏng giao tiếp giữa các đối
   tượng mà không biết về sự tồn tại của nhau. Điều này có ích trong các tình huống khi bạn muốn giảm sự ràng buộc giữa
   các thành phần trong hệ thống.

## Khi nào thì sử dụng mediator

Mediator design pattern được sử dụng khi bạn muốn giảm sự phụ thuộc giữa các thành phần trong một hệ thống phức tạp và
thay thế chúng bằng sự giao tiếp thông qua một đối tượng trung gian (mediator). Điều này giúp làm cho hệ thống dễ bảo
trì, mở rộng và thay đổi, vì bạn chỉ cần thay đổi mediator thay vì sửa đổi nhiều thành phần riêng lẻ.
Dưới đây là một số tình huống thường gặp khi bạn nên sử dụng Mediator design pattern:

1. **Hệ thống có nhiều đối tượng giao tiếp một cách phức tạp:** Khi có nhiều đối tượng cần giao tiếp với nhau và sự phức
   tạp của các mối quan hệ giao tiếp này tăng lên, sử dụng Mediator giúp giảm sự rắc rối và tạo ra một điểm trung tâm để
   quản lý tất cả các tương tác.
2. **Sự phụ thuộc giữa các đối tượng:** Khi các đối tượng trong hệ thống có sự phụ thuộc mạnh mẽ vào nhau, sử dụng
   Mediator giúp loại bỏ sự phụ thuộc này và tạo ra một lớp trung gian để quản lý việc giao tiếp.
3. **Tính tái sử dụng và mở rộng:** Mediator giúp tạo ra một kiến trúc linh hoạt cho hệ thống, dễ dàng thêm mới các đối
   tượng và thay đổi cách chúng tương tác mà không ảnh hưởng đến các phần còn lại của hệ thống.
4. **Giảm sự phức tạp của các đối tượng:** Mediator cho phép chia nhỏ sự phức tạp của các đối tượng thành các phần nhỏ
   hơn, giúp quản lý và hiểu được cách chúng hoạt động.
5. **Mô phỏng giao tiếp giữa các thành phần không biết về nhau:** Khi bạn muốn mô phỏng giao tiếp giữa các đối tượng mà
   không muốn chúng biết về sự tồn tại của nhau.

## Running

```
python main.py
python example.py
```