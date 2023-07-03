using System;
using System.Drawing;

class Program {
    static void Main() {

        // Carrega a imagem
        Bitmap imagemOriginal = new Bitmap("C:_Users\01285745000_Desktop_imagens jpg_Lenna.jpg");

        // Converte a imagem para escala de cinza
        Bitmap imagemCinza = ConverterParaEscalaCinza(imagemOriginal);

        // Aplica o filtro de Wiener na imagem
        Bitmap imagemFiltrada = AplicarFiltroWiener(imagemCinza);

        // Exibe a imagem original e a imagem filtrada
        ExibirImagem(imagemOriginal, "Imagem Original");
        ExibirImagem(imagemFiltrada, "Imagem Filtrada");
    }

    // Converte uma imagem colorida para a escala de cinza
    static Bitmap ConverterParaEscalaCinza (Bitmap imagem) {
        Bitmap imagemCinza = new Bitmap(imagem.Width, imagem.Height);

        for (int y = 0; y < imagem.Height; y++) {
            for (int x = 0; x < imagem.Width; x++) {
                Color pixel = imagem.GetPixel(x, y);

                // Calcula o valor de cinza como a média dos valores RGB
                int valorCinza = (pixel.R + pixel.G + pixel.B) / 3;

                // Cria um novo pixel em escala de cinza
                Color novoPixel = Color.FromArgb(valorCinza, valorCinza, valorCinza);

                // Define o novo pixel na imagem em escala de cinza
                imagemCinza.SetPixel(x, y, novoPixel);
            }
        }

        return imagemCinza;
    }

    // Aplica o filtro de Wiener em uma imagem em escala de cinza
    static Bitmap AplicarFiltroWiener(Bitmap imagem) {

        // Define os parâmetros do filtro de Wiener
        double snr = 10; // Relação sinal-ruído
        double K = 1.0 / snr;

        int width = imagem.Width;
        int height = imagem.Height;

        Bitmap imagemFiltrada = new Bitmap(width, height);

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                double somatorio = 0;
                double denominador = 0;

                // Percorre a vizinhança do pixel
                for (int j = -1; j <= 1; j++) {
                    for (int i = -1; i <= 1; i++) {
                        int posX = x + i;
                        int posY = y + j;

                        //  Verifica se a posição está dentro dos limites da imagem
                        if (posX >= 0 && posX < width && posY >= 0 && posY < height) {
                            Color pixel = imagem.GetPixel(posX, posY);

                            // Obtém o valor de cinza do pixel
                            double valorCinza = pixel.R;

                            // Calcula o peso do pixel
                            double peso = Math.Exp(-(i * i + j * j) / (2 * K * K));

                            somatorio += valorCinza * peso;
                            denominador += peso;
                        }
                    }
                }

                // Calcula o valor do pixel filtrado
                int valorFiltrado = (int)Math.Round(somatorio / denominador);

                // Define o pixel filtrado na imagem
                Color novoPixel = Color.FromArgb(valorFiltrado, valorFiltrado, valorFiltrado);
                imagemFiltrada.SetPixel(x, y, novoPixel);
            }
        }

        return imagemFiltrada;
    }

    // Exibe uma imagem em uma nova janela
    static void ExibirImagem(Bitmap imagem, string titulo) {
        
        // Cria uma nova janela para exibir a imagem
        Form janela = new Form();
        janela.Text = titulo;
        janela.ClientSize = imagem.Size;

        // Cria um controle PictureBox para exibir a imagem
        PictureBox pictureBox = new PictureBox();
        pictureBox.Dock = DockStyle.Fill;
        pictureBox.Image = imagem;

        // Adiciona o controle PictureBox à janela
        janela.Controls.Add(pictureBox);

        // Exibe a janela
        Application.Run(janela);
    }
}