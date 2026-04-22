from src.services.consumer import Consumer
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("=== Iniciando o Robô RPA Challenge ===")
    
    try:
        robo = Consumer()
        robo.fill_out_the_web_form()
        
    except Exception as e:
        logger.critical(f"Erro fatal não tratado na execução principal: {e}", exc_info=True)
        
    finally:
        logger.info("=== Fim da execução do Robô ===")


if __name__ == "__main__":
    main()