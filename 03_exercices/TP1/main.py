from test_dropdown import test_dropdown
from test_log_in_out import test_login_logout
from test_remove_add_element import test_add_remove_elements

def main():
    print("\n" + "=" * 60)
    print("CORRECTION TP1 - SELENIUM PYTHON POM")
    print("=" * 60)

    try:
        test_login_logout()
        test_dropdown()
        test_add_remove_elements()

        print("\n" + "=" * 60)
        print("Tous les tests du TP1 sont passés")
        print("=" * 60)
    
    except Exception as e:
        print(f"\n Echec global du TP1 : {e}")



if __name__ == "__main__":
    main()


