class PriceTrackerError(Exception):
    pass

class WebScrapingError(PriceTrackerError):
    pass

class FileOperationError(PriceTrackerError):
    pass

class DataValidationError(PriceTrackerError):
    pass


