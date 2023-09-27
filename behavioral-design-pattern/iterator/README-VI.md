## Source

https://refactoring.guru/design-patterns/iterator

## Cốt lõi:

> Iterator là một mẫu thiết kế hành vi cho phép bạn duyệt qua các phần tử của một tập hợp mà không tiết lộ cấu trúc dữ
> liệu cơ bản của nó (danh sách, ngăn xếp, cây, vv.).

## Structure

![alt tag](iterator.png)

Các bước tạo iterator chính:

1. **Xác định Interface Iterator:** Đầu tiên, bạn cần xác định một interface Iterator, mô tả các phương thức cần thiết
   để duyệt qua tập hợp. Interface này thường bao gồm các phương thức như hasNext() để kiểm tra xem còn phần tử tiếp
   theo hay không và next() để lấy phần tử tiếp theo.
2. **Xác định Interface Aggregate (Interface Aggregate):** Bạn cũng cần xác định một interface Aggregate (hoặc có thể
   gọi là Container) mô tả cách tạo ra một Iterator cho tập hợp. Iterface này thường chứa một phương thức có tên là
   createIterator() hoặc tương tự.
3. **Triển khai Aggregate (Container):** Tạo một lớp triển khai interface Aggregate để định nghĩa tập hợp và cách tạo
   Iterator cho tập hợp đó. Lớp này thường bao gồm một danh sách (hoặc cấu trúc dữ liệu khác) để lưu trữ các phần tử
   trong tập hợp và triển khai phương thức createIterator() để tạo ra một Iterator tương ứng.
4. **Triển khai Iterator:** Tạo một hoặc nhiều lớp triển khai interface Iterator để duyệt qua các phần tử của tập hợp.
   Lớp Iterator này thường cần lưu trữ tham chiếu đến Aggregate và triển khai các phương thức hasNext() và next() để
   điều khiển việc duyệt qua các phần tử.
5. **Sử dụng Iterator trong Client Code:** Trong client code, tạo một đối tượng Aggregate (tập hợp) và sau đó sử dụng
   phương thức createIterator() để tạo một Iterator. Sau đó, bạn có thể sử dụng Iterator để duyệt qua các phần tử của
   tập hợp mà không cần biết chi tiết về cấu trúc nội bộ của tập hợp.
6. **Tạo các lớp cụ thể của tập hợp (tuỳ chọn):** Nếu bạn cần duyệt qua các loại tập hợp khác nhau, bạn có thể tạo các
   lớp cụ thể của tập hợp và triển khai interface Aggregate cho từng loại tập hợp đó.

## Description

### Mục đích

1. **Tách biệt giao diện duyệt qua (traversal) và cấu trúc tập hợp:** Iterator giúp bạn tách biệt việc duyệt qua các
   phần tử từ cấu trúc dữ liệu của tập hợp. Điều này giúp giảm sự phụ thuộc giữa các phần tử của tập hợp và client code,
   cho phép bạn thay đổi cấu trúc tập hợp mà không cần sửa đổi client code.
2. **Giấu đi chi tiết triển khai của tập hợp:** Iterator che giấu chi tiết về cách tập hợp được triển khai bên trong.
   Điều này làm cho client code không cần biết về cấu trúc cụ thể của tập hợp và không phụ thuộc vào nó.
3. **Hỗ trợ nhiều cách duyệt qua:** Iterator cho phép bạn có nhiều loại Iterator khác nhau để duyệt qua tập hợp, mà
   không cần thay đổi client code. Bạn có thể cung cấp các Iterator tùy chỉnh để duyệt qua các phần tử theo cách riêng
   của mình.
4. **Hỗ trợ duyệt qua ngược (reverse traversal):** Bạn có thể triển khai Iterator để hỗ trợ duyệt qua tập hợp theo chiều
   ngược lại mà không cần sửa đổi tập hợp.
5. **Duyệt qua tập hợp một cách không phụ thuộc vào loại cấu trúc dữ liệu:** Iterator cho phép bạn duyệt qua các tập hợp
   dữ liệu khác nhau một cách đồng nhất. Điều này làm cho code của bạn có thể linh hoạt hơn và có thể sử dụng lại cho
   nhiều loại tập hợp khác nhau.
6. **Hỗ trợ các thao tác duyệt qua an toàn:** Iterator Pattern cho phép bạn duyệt qua các phần tử của tập hợp một cách
   an toàn mà không làm thay đổi cấu trúc của tập hợp.

## Khi nào thì sử dụng iterator

1. **Khi bạn muốn duyệt qua các phần tử trong một tập hợp:** Iterator cho phép bạn duyệt qua các phần tử của tập hợp một
   cách tuần tự, mà không cần biết cấu trúc nội bộ của tập hợp.
2. **Khi bạn muốn tách biệt code duyệt qua và cấu trúc tập hợp:** Iterator giúp tách biệt phần code duyệt qua các phần
   tử và cấu trúc dữ liệu của tập hợp. Điều này giúp giảm sự phụ thuộc giữa các phần tử của tập hợp và client code, cho
   phép bạn thay đổi cấu trúc tập hợp mà không làm thay đổi client code.
3. **Khi bạn muốn hỗ trợ nhiều cách duyệt qua:** Iterator cho phép bạn triển khai nhiều loại Iterator khác nhau để duyệt
   qua tập hợp theo cách riêng của mình. Điều này hữu ích khi bạn cần duyệt qua tập hợp theo nhiều cách khác nhau.
4. **Khi bạn muốn hỗ trợ duyệt qua ngược:** Iterator cung cấp một cách tiêu chuẩn để hỗ trợ duyệt qua tập hợp theo chiều
   ngược lại (reverse traversal).
5. **Khi bạn muốn duyệt qua các tập hợp dữ liệu khác nhau một cách đồng nhất:** Iterator cho phép bạn duyệt qua các tập
   hợp dữ liệu khác nhau một cách đồng nhất bằng cách sử dụng cùng một giao diện Iterator. Điều này giúp code của bạn
   trở nên linh hoạt và có thể tái sử dụng cho nhiều loại tập hợp khác nhau.
6. **Khi bạn muốn duyệt qua các phần tử của tập hợp một cách an toàn:** Iterator cho phép bạn duyệt qua các phần tử của
   tập hợp một cách an toàn mà không làm thay đổi cấu trúc của tập hợp, đảm bảo tính toàn vẹn của dữ liệu.
7. **Khi bạn muốn làm cho code của bạn dễ đọc và bảo trì hơn:** Sử dụng Iterator giúp bạn tách biệt code duyệt qua phần
   code xử lý các phần tử. Điều này làm cho code của bạn trở nên dễ đọc hơn và dễ bảo trì hơn.

## Running

```
python main.py
python example.py
```