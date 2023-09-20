## Source

https://refactoring.guru/design-patterns/bridge

## Cốt lõi:

> Composite là một mẫu thiết kế cấu trúc cho phép bạn kết hợp các đối tượng thành cấu trúc cây và sau đó làm việc với
> cấu trúc này như là các đối tượng độc lập.

## Structure

![alt tag](adapter.png)

Các bước tạo một composite

1. **Xác định interface hoặc abstract class:** Đầu tiên, bạn cần xác định một interface hoặc abstract class chung cho
   tất cả
   các đối tượng trong cây composite. Điều này đảm bảo rằng tất cả các thành phần trong cây có thể được xử lý một cách
   thống nhất.
2. **Tạo lớp cơ sở:** Tạo một lớp cơ sở hoặc interface chung cho các đối tượng lá và đối tượng composite. Lớp cơ sở này
   sẽ
   chứa các phương thức chung mà tất cả các thành phần cần phải triển khai.
3. **Triển khai các đối tượng lá:** Tạo các lớp con (subclasses) cho các đối tượng lá (leaf objects) trong cây. Các đối
   tượng lá không có các con, nói cách khác, chúng không thể chứa các thành phần con khác.
4. **Triển khai các đối tượng composite:** Tạo các lớp con (subclasses) cho các đối tượng composite. Các đối tượng
   composite
   có thể chứa các thành phần con khác, bao gồm cả các đối tượng lá và các đối tượng composite khác.
5. **Xây dựng cây composite:** Sử dụng các đối tượng lá và composite đã được triển khai để xây dựng cây composite. Cây
   này
   có thể có cấu trúc phức tạp với các thành phần con chứa các thành phần con khác.
6. **Triển khai phương thức thao tác:** Trong lớp cơ sở hoặc interface chung, triển khai các phương thức để thêm, xóa
   hoặc
   duyệt qua các thành phần trong cây composite. Điều này cho phép bạn thao tác với cây composite một cách thống nhất mà
   không cần quan tâm đến sự khác biệt giữa các đối tượng lá và composite.

## Description

### Mục đích

1. **Xây dựng cây đối tượng phức tạp:** Cho phép bạn xây dựng cây đối tượng phức tạp bằng cách kết hợp các đối tượng đơn
   giản và đối tượng composite. Cây này có thể có cấu trúc cây và chứa các đối tượng lá và các đối tượng composite khác.
2. **Thao tác thống nhất:** Giúp bạn thực hiện các thao tác trên cả cây đối tượng và các phần của cây một cách thống
   nhất. Bạn có thể gọi các phương thức trên đối tượng composite mà không cần quan tâm đến việc nó có phải là một đối
   tượng lá hay một đối tượng composite.
3. **Tái sử dụng và linh hoạt:** Mẫu Composite cho phép bạn tái sử dụng mã và tạo ra các cây đối tượng có cấu trúc khác
   nhau mà không cần thay đổi mã nguồn cốt lõi. Bạn có thể thêm hoặc loại bỏ các thành phần một cách dễ dàng.
4. **Đảm bảo tính đối xứng:** Mẫu này giúp đảm bảo tính đối xứng trong cấu trúc cây đối tượng. Cả đối tượng lá và đối
   tượng composite đều tuân theo cùng một interface hoặc lớp cơ sở, giúp tạo sự thống nhất trong cấu trúc.
5. **Giảm thiểu sự phức tạp:** Khi bạn cần làm việc với cấu trúc dữ liệu phức tạp, mẫu Composite giúp giảm thiểu sự phức
   tạp của mã bằng cách tổ chức các thành phần trong cây và cho phép bạn xử lý chúng theo cách thống nhất.

Mẫu Composite thường được sử dụng trong các tình huống mà bạn cần biểu diễn các đối tượng có cấu trúc cây hoặc cây phân
cấp, chẳng hạn như biểu diễn interface người dùng đồ họa, biểu diễn cấu trúc tài liệu, hoặc trong việc quản lý danh sách
và cây thư mục trong hệ thống tệp tin.

## Khi nào thì sử dụng composite

1. **Cây đối tượng có cấu trúc cây hoặc phân cấp:** Khi bạn cần biểu diễn một cây đối tượng mà có thể chứa các đối tượng
   lá và các đối tượng composite khác. Ví dụ bao gồm cấu trúc tài liệu, cây DOM trong lập trình web, cây thư mục và tệp
   trong hệ thống tệp tin.
2. **Thao tác trên toàn bộ cấu trúc:** Khi bạn cần thực hiện các thao tác trên toàn bộ cấu trúc cây hoặc phân cấp một
   cách thống nhất, ví dụ như duyệt qua tất cả các phần tử hoặc thực hiện một thao tác trên tất cả các nút của cây.
3. **Tái sử dụng mã và linh hoạt:** Khi bạn muốn có khả năng tái sử dụng mã để xây dựng và quản lý các cây đối tượng có
   cấu trúc khác nhau mà không cần thay đổi mã nguồn cốt lõi.
4. **Đảm bảo tính đối xứng và thống nhất:** Khi bạn muốn đảm bảo tính đối xứng trong cấu trúc cây đối tượng, đồng thời
   cho phép bạn thực hiện các thao tác trên các thành phần trong cây một cách thống nhất.
5. **Giảm thiểu sự phức tạp:** Khi bạn muốn giảm thiểu sự phức tạp của mã khi làm việc với cấu trúc dữ liệu phức tạp,
   chẳng hạn như trong việc quản lý giao diện người dùng đồ họa có cấu trúc phân cấp.
6. **Phân tách cấu trúc và hành vi:** Khi bạn muốn tách riêng cấu trúc của các đối tượng và hành vi của chúng, cho phép
   bạn thêm các thành phần mới mà không làm thay đổi cấu trúc hiện có.
7. **Phát triển theo nguyên tắc "Đơn trách nhiệm" (Single Responsibility Principle):** Khi bạn muốn mỗi đối tượng chỉ
   phải chịu trách nhiệm cho một nhiệm vụ cụ thể trong cấu trúc cây và không phải biết về cấu trúc toàn bộ cây.
8. **Mở rộng cấu trúc một cách dễ dàng:** Khi bạn muốn có khả năng mở rộng cấu trúc cây đối tượng một cách dễ dàng bằng
   cách thêm các thành phần mới.

Tóm lại, bạn nên sử dụng mẫu thiết kế Composite khi bạn có cấu trúc dữ liệu cây phức tạp và muốn thực hiện các thao tác
trên cấu trúc đó một cách thống nhất và linh hoạt.

## Running

```
python main.py
python example.py
```