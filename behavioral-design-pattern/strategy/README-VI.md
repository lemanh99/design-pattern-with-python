## Source

https://refactoring.guru/design-patterns/strategy

## Cốt lõi:

> Mẫu thiết kế Strategy là một mẫu thiết kế hành vi cho phép bạn định nghĩa một họ (family) các thuật toán, đặt mỗi
> thuật toán vào một lớp riêng biệt và làm cho các đối tượng của chúng trở nên có thể hoán đổi được.

## Structure

![alt tag](strategy.png)

Các bước tạo strategy chính:

1. Xác định hành vi cần thay đổi:

- Xác định hành vi hoặc thuật toán mà bạn muốn tạo thành chiến lược (strategy). Điều này thường liên quan đến các phần
  của mã của bạn mà bạn muốn thay đổi tùy thuộc vào yêu cầu cụ thể.

2. Tạo giao diện hoặc lớp cơ sở (Interface or Base Class):

- Định nghĩa một giao diện (interface) hoặc lớp cơ sở (base class) chung cho tất cả các chiến lược. Giao diện hoặc lớp
  này sẽ chứa phương thức hoặc hành vi chung cho tất cả các chiến lược.

3. Triển khai các chiến lược (Concrete Strategies):

- Tạo các lớp con triển khai giao diện hoặc kế thừa từ lớp cơ sở đã định nghĩa ở bước trước. Mỗi lớp này sẽ triển khai
  cách thực hiện cụ thể của chiến lược.

4. Tạo đối tượng Context:

- Tạo một lớp chứa đối tượng chiến lược và các phương thức để thiết lập và thay đổi chiến lược. Lớp này được gọi là "
  Context."

5. Thêm phương thức cho Context để thay đổi chiến lược:

- Trong lớp Context, bạn cần thêm các phương thức để thiết lập chiến lược và gọi hành vi tương ứng từ chiến lược. Thường
  có một phương thức để thiết lập chiến lược và một hoặc nhiều phương thức để thực hiện hành vi tùy thuộc vào chiến
  lược.

6. Sử dụng Mẫu Strategy:

- Tạo đối tượng Context và thiết lập chiến lược mặc định hoặc khởi tạo với một chiến lược cụ thể. Sau đó, sử dụng các
  phương thức của Context để thực hiện hành vi và thay đổi chiến lược nếu cần.

## Description

### Mục đích

Mục đích chính của Mẫu thiết kế Strategy (Strategy Design Pattern) là cho phép bạn định nghĩa một tập hợp các thuật toán
hoặc chiến lược khác nhau, đóng gói chúng thành các đối tượng riêng biệt và cho phép bạn lựa chọn và thay đổi chiến lược
mà đối tượng sử dụng trong thời gian chạy một cách linh hoạt và độc lập. Dưới đây là mục đích cụ thể của Mẫu Strategy:

1. **Tách biệt chiến lược từ đối tượng chứa nó:** Strategy giúp tách biệt các thuật toán hoặc chiến lược khỏi đối tượng
   sử dụng chúng. Điều này giúp giảm sự phức tạp của đối tượng chứa và cho phép tái sử dụng chiến lược cho nhiều đối
   tượng khác nhau.
2. **Cho phép lựa chọn tại thời điểm chạy:** Strategy cho phép bạn thay đổi hành vi của một đối tượng tại thời điểm
   chạy, thay vì phải thiết kế lại hoặc sửa đổi mã nguồn. Điều này rất hữu ích khi bạn cần lựa chọn giữa nhiều biến thể
   của một hành vi cụ thể.
3. **Loại bỏ sự phụ thuộc vào IF-ELSE lồng nhau:** Strategy giúp thay thế các câu lệnh IF-ELSE lồng nhau mà bạn thường
   gặp trong mã nguồn bằng cách cung cấp một cách sắp xếp dễ quản lý các chiến lược riêng biệt.
4. **Tạo mã linh hoạt và dễ bảo trì:** Strategy tạo ra mã dễ đọc, dễ bảo trì và dễ mở rộng. Bạn có thể thêm mới các
   chiến lược mới mà không cần sửa đổi mã hiện tại, giúp giảm nguy cơ gây lỗi và tăng khả năng tái sử dụng.
5. **Chia sẻ hành vi giữa nhiều đối tượng:** Strategy cho phép bạn chia sẻ một chiến lược giữa nhiều đối tượng khác
   nhau, giúp tối ưu hóa sử dụng tài nguyên và giảm lặp lại mã.
6. **Định nghĩa giao diện chung cho các chiến lược:** Strategy thường định nghĩa một giao diện hoặc lớp cơ sở chung cho
   các chiến lược, tạo điều kiện cho tính đa hình và cho phép bạn thay đổi chiến lược mà không ảnh hưởng đến giao diện
   của đối tượng.

## Khi nào thì sử dụng strategy

Mẫu thiết kế Strategy (Strategy Design Pattern) thường được sử dụng trong các tình huống sau:

1. **Khi bạn muốn chọn giữa nhiều thuật toán tương đương:** Strategy cho phép bạn định nghĩa một tập hợp các thuật toán
   khác nhau và chọn một trong số chúng dựa trên yêu cầu cụ thể hoặc điều kiện hiện tại.
2. **Khi bạn muốn loại bỏ các điều kiện IF-ELSE lồng nhau:** Thay vì sử dụng nhiều câu lệnh IF-ELSE để kiểm tra điều
   kiện và thực hiện hành vi tương ứng, bạn có thể sử dụng Strategy để tạo ra một chiến lược riêng biệt cho mỗi tùy
   chọn, từ đó giảm sự phức tạp của mã.
3. **Khi bạn muốn cung cấp một giao diện duy nhất cho các hành vi khác nhau:** Strategy cho phép bạn định nghĩa một giao
   diện chung cho tất cả các chiến lược và sau đó triển khai các chi tiết cụ thể riêng biệt cho mỗi chiến lược. Điều này
   tạo ra tính linh hoạt và cho phép bạn thay đổi chiến lược mà không cần thay đổi giao diện.
4. **Khi bạn muốn tránh việc sửa đổi mã hiện tại khi thêm hoặc thay đổi hành vi:** Strategy cho phép bạn thêm mới hoặc
   thay đổi chiến lược mà không cần sửa đổi mã hiện tại, do đó giảm nguy cơ gây lỗi và tăng tính bảo trì.
5. **Khi bạn muốn tách biệt phần xử lý của một đối tượng khỏi nó:** Strategy cho phép bạn tách biệt logic xử lý ra khỏi
   đối tượng chứa nó, từ đó giúp bạn duy trì sự đơn giản và dễ bảo trì của mã.
6. **Khi bạn muốn chia sẻ hành vi giữa nhiều đối tượng:** Strategy cho phép bạn chia sẻ một chiến lược giữa nhiều đối
   tượng, do đó tối ưu hóa sử dụng tài nguyên.

Ví dụ phổ biến của việc sử dụng Mẫu Strategy bao gồm quản lý các thuật toán sắp xếp (ví dụ: sắp xếp nhanh, sắp xếp chèn,
sắp xếp nổi bọt), quản lý các chiến lược thanh toán (ví dụ: thanh toán bằng thẻ tín dụng, thanh toán qua PayPal), quản
lý các chiến lược quảng cáo (ví dụ: quảng cáo trả phí, quảng cáo miễn phí), và nhiều tình huống khác.

## Running

```
python main.py
python example.py
```