class klasa1 extends klasa0<klasa1>
{
    public klasa1(String nazwisko, java.time.LocalDate rokUrodzenia, double sredniaOcen)
    {
        super(nazwisko,rokUrodzenia);
        this.sredniaOcen= sredniaOcen;
    }

    public String getSredniaOcen()
    {
        return String.valueOf(this.sredniaOcen);
    }
    public void setSredniaOcen(double Srednia)
    {
        this.sredniaOcen = Srednia;
    }

    @Override
    public String toString() {
        return "Osoba" +
                "[rokUrodzenia=" + super.getRokUrodzenia() +
                "], [nazwisko=" + super.getNazwisko() +
                "], [srednia=" + sredniaOcen +
                ']';
    }

    private double sredniaOcen;
    public int compareTo(klasa1 o) {
        String str1=this.toString();
        String str2=o.toString();
        if (str1.length()>str2.length())
            return 1;
        else if (str1.length()<str2.length())
            return -1;
        else
            return 0;
    }
}