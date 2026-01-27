# ROS 2 Python Project: my_py_pkg

Bu repo, **ROS 2 Humble** üzerinde geliştirilen temel bir Python düğümü (node) uygulamasıdır. İçerisinde Nesne Yönelimli Programlama (OOP) prensipleriyle oluşturulmuş, zamanlayıcı (timer) ve loglama mekanizmalarını içeren bir yapı barındırır.

## 🚀 Başlangıç

Bu paketi yerel makinenizde çalıştırmak için aşağıdaki gereksinimleri karşılamanız ve kurulum adımlarını izlemeniz gerekir.

### Sistem Gereksinimleri
* **İşletim Sistemi:** Ubuntu 22.04 (Jammy Jellyfish)
* **ROS 2 Versiyonu:** Humble Hawksbill
* **Araçlar:** `colcon`, `python3`, `rclpy`, `Git`

### Kurulum

1.  **Workspace oluşturun ve repoyu klonlayın:**
    ```bash
    mkdir -p ~/ros2YT_ws/src
    cd ~/ros2YT_ws/src
    git clone <repo-url-buraya-gelecek>
    ```

2.  **Bağımlılıkları kontrol edin:**
    ```bash
    cd ~/ros2YT_ws
    rosdep install -i --from-path src --rosdistro humble -y
    ```

3.  **Projeyi derleyin (Build):**
    ```bash
    colcon build --packages-select my_py_pkg
    ```

---

## 💻 Kullanım

Derleme işlemi bittikten sonra, terminalin bu paketi tanıması için `setup.bash` dosyasını `source` etmeniz gerekir:

```bash
source install/setup.bash
ros2 run my_py_pkg py_node
