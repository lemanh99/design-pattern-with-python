## Source

https://refactoring.guru/design-patterns/builder

## Cốt lõi:

>Builder là một mẫu thiết kế sáng tạo cho phép bạn xây dựng đối tượng phức tạp bước từng bước. Mẫu thiết kế này cho phép bạn tạo ra các loại và biểu diễn khác nhau của một đối tượng bằng cách sử dụng mã xây dựng chung.

## Structure

![alt tag](builder.png)

Các bước tạo builder pattern chính:
1. **Xác định lớp đối tượng cần build (Product)**
2. **Tạo lớp Builder:** Tạo một lớp Builder tương ứng cho lớp đối tượng cần xây dựng. Lớp Builder này sẽ chứa các phương thức để thiết lập các thuộc tính của đối tượng đích.
3. **Thêm method để thiết lập thuộc tính trong lớp Builder:** Trong lớp Builder, bạn cần thêm các phương thức để thiết lập các thuộc tính của đối tượng đích. Mỗi phương thức sẽ trả về chính lớp Builder để cho phép việc gọi phương thức liên tiếp (method chaining).
4. **Tạo phương thức build() trong lớp Builder:** Phương thức build() sẽ trả về một đối tượng đã hoàn thiện sau khi tất cả các thuộc tính cần thiết đã được thiết lập trong lớp Builder. Phương thức này có thể tạo một đối tượng mới hoặc trả về đối tượng hiện có nếu bạn muốn chỉnh sửa nó.
5. **Tạo lớp Director (tuỳ chọn):** Lớp Director có thể được sử dụng để quản lý quá trình xây dựng đối tượng bằng cách sử dụng lớp Builder. Trong một số trường hợp, bạn có thể có một lớp Director để tự động hóa việc xây dựng đối tượng.
6. **Sử dụng Builder để xây dựng đối tượng:** Trong source của bạn, sử dụng lớp Builder để xây dựng đối tượng. Bắt đầu bằng việc tạo một thể hiện của lớp Builder, sau đó sử dụng các phương thức thiết lập thuộc tính và cuối cùng gọi phương thức build() để nhận đối tượng hoàn thiện.

## Description

### Mục đích

Builder là một mẫu thiết kế (design pattern) trong lập trình, thường được sử dụng để xây dựng các đối tượng phức tạp
bằng cách chia chúng thành các phần nhỏ hơn và sau đó xây dựng chúng bước từng bước. Mục đích chính của mẫu thiết kế
Builder là tách rời quá trình xây dựng đối tượng khỏi cách thức đối tượng được xây dựng. Dưới đây là một số mục đích cụ
thể của Builder pattern:

1. **Tạo đối tượng phức tạp:** Builder pattern giúp bạn tạo ra các đối tượng phức tạp bằng cách tổ hợp nhiều phần khác
   nhau. Thay vì xây dựng trực tiếp đối tượng từng phần, bạn có thể sử dụng một builder để thực hiện quá trình này một
   cách dễ dàng và kiểm soát hơn.
2. **Tạo đối tượng có thể thay đổi**: Mẫu Builder cho phép bạn tạo ra các đối tượng mà các thuộc tính của chúng có thể
   thay đổi theo ý muốn. Bạn có thể cung cấp các phương thức để thay đổi giá trị của các thuộc tính trong quá trình xây
   dựng.
3. **Giảm sự phức tạp:** Builder pattern giúp giảm đi sự phức tạp của việc xây dựng đối tượng bằng cách tạo ra một quá
   trình xây dựng có cấu trúc và kiểm soát. Điều này làm cho mã nguồn dễ đọc hơn và dễ bảo trì hơn, đặc biệt khi bạn có
   nhiều tùy chọn và biến thể cho một đối tượng.
4. **Tách rời việc xây dựng và biểu diễn**: Builder pattern tách rời quá trình xây dựng đối tượng và việc biểu diễn của
   nó. Điều này có nghĩa rằng bạn có thể sử dụng cùng một quá trình xây dựng để tạo các biểu diễn khác nhau của đối
   tượng, chẳng hạn như biểu diễn JSON, XML hoặc HTML khác nhau từ cùng một đối tượng dữ liệu.
5. **Hỗ trợ cho việc xây dựng đối tượng phức tạp và có quy trình khác nhau**: Builder pattern cho phép bạn xây dựng các
   đối tượng phức tạp và có quy trình xây dựng khác nhau mà không cần thay đổi cấu trúc của đối tượng.

Tóm lại, Builder pattern giúp tạo ra các đối tượng phức tạp một cách linh hoạt, kiểm soát quá trình xây dựng và giảm sự
phức tạp của mã nguồn. Điều này làm cho mã nguồn dễ đọc, bảo trì và mở rộng hơn trong các trường hợp cần xây dựng các
đối tượng phức tạp và có nhiều tùy chọn.

## Khi nào thì sử dụng builder pattern
1. **Khi bạn muốn xây dựng các đối tượng phức tạp:** Khi đối tượng bạn đang cố gắng xây dựng có nhiều thuộc tính hoặc tùy chọn khác nhau và việc khởi tạo chúng trở nên rất phức tạp, Builder pattern giúp bạn tạo ra các đối tượng này một cách dễ dàng và linh hoạt.
2. **Khi bạn muốn tạo ra các biểu diễn khác nhau của đối tượng:** Builder pattern cho phép bạn tạo ra nhiều biểu diễn (representation) của cùng một đối tượng dữ liệu. Ví dụ, bạn có thể tạo đối tượng từ dữ liệu và sau đó sử dụng các builder khác nhau để tạo các biểu diễn JSON, XML, hoặc HTML từ cùng một dữ liệu.
3. **Khi bạn muốn tách rời quá trình xây dựng và biểu diễn:** Builder pattern cho phép bạn tách rời quá trình xây dựng đối tượng và việc biểu diễn của nó. Điều này giúp bạn thay đổi cách thức biểu diễn mà không ảnh hưởng đến cấu trúc của đối tượng.
4. **Khi bạn muốn kiểm soát quá trình xây dựng đối tượng:** Builder pattern cho phép bạn kiểm soát quá trình xây dựng đối tượng bằng cách cung cấp các phương thức cho phép thay đổi giá trị của các thuộc tính trong quá trình xây dựng.
5. **Khi bạn muốn tránh sử dụng constructor có quá nhiều tham số:** Khi có quá nhiều tham số trong constructor của một lớp, việc sử dụng builder pattern giúp tránh việc tạo ra các constructor có quá nhiều tham số (constructor hell).
6. **Khi bạn muốn cải thiện độ đọc và bảo trì của mã nguồn:** Builder pattern làm cho mã nguồn trở nên dễ đọc hơn, đặc biệt khi bạn cần xây dựng các đối tượng phức tạp và có nhiều tùy chọn.

Tóm lại, sử dụng Builder pattern khi bạn đối diện với việc xây dựng đối tượng phức tạp, cần tạo ra các biểu diễn khác nhau của đối tượng, muốn tách rời quá trình xây dựng và biểu diễn, hoặc muốn kiểm soát quá trình xây dựng một cách chi tiết và linh hoạt hơn.

## Running

```
python main.py
python example.py
```