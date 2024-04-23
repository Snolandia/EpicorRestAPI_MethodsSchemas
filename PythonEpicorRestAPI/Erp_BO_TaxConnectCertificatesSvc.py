import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxConnectCertificatesSvc
# Description: Business Object that handled Tax Connect Certificate Logic
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetTaxConnectCertificates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxConnectCertificates
   Description: Retrieves list of Avalara CertCapture Certificates for a specific customer.
   OperationID: GetTaxConnectCertificates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxConnectCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxConnectCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadTaxConnectCertificatePreview(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadTaxConnectCertificatePreview
   Description: Get the first page of the Certificate
   OperationID: DownloadTaxConnectCertificatePreview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadTaxConnectCertificatePreview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadTaxConnectCertificatePreview_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SendCustomerToTaxConnect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SendCustomerToTaxConnect
   Description: Upload customer information to Avalara
   OperationID: SendCustomerToTaxConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendCustomerToTaxConnect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendCustomerToTaxConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RequestTaxConnectCertificateCustomerInvite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RequestTaxConnectCertificateCustomerInvite
   Description: Trigger an email certificate invite from avalara to the customer
   OperationID: RequestTaxConnectCertificateCustomerInvite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RequestTaxConnectCertificateCustomerInvite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestTaxConnectCertificateCustomerInvite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DownloadTaxConnectCertificatePreview_input:
   """ Required : 
   certificateID
   """  
   def __init__(self, obj):
      self.certificateID:int = obj["certificateID"]
      """  Avalara Certificate ID  """  
      pass

class DownloadTaxConnectCertificatePreview_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Certificate first page in base64  """  
      pass

class Erp_Tablesets_TaxConnectCertificatesRow:
   def __init__(self, obj):
      self.BusinessNumberType:str = obj["BusinessNumberType"]
      """  Description of business for the certificate. For example, Retail trade, Professional services, or Construction.  """  
      self.CertificateID:int = obj["CertificateID"]
      """  Unique ID number of this certificate.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  The date/time when this record was created.  """  
      self.DocumentExists:bool = obj["DocumentExists"]
      """  This value is true if there exists a scanned PDF copy of this certificate or the PDF version of the form that the customer filled via the CertCapture wizard on S3 bucket.  """  
      self.ExemptionNumber:str = obj["ExemptionNumber"]
      """  Indicates the tax number passed in for the certificate.  """  
      self.ExemptPercentage:int = obj["ExemptPercentage"]
      """   If this certificate provides exemption from transactional taxes, what percentage of the transaction is considered exempt?

For a fully exempt certificate, this percentage should be 100.  """  
      self.ExemptReason:str = obj["ExemptReason"]
      """  The exemption reason associated with this certificate. For example, the reason code for exemption for purposes of resale is RESALE.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Expiration date when this certificate will no longer be valid.  """  
      self.Filename:str = obj["Filename"]
      """  File name for the image of this certificate.  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  The date/time when this record was last modified.  """  
      self.PageCount:int = obj["PageCount"]
      """  Number of pages contained within this certificate.  """  
      self.Region:str = obj["Region"]
      """  The exposure zone/region where this certificate is valid.  """  
      self.SignedDate:str = obj["SignedDate"]
      """  The date when this certificate was signed.  """  
      self.Status:str = obj["Status"]
      """  The status of the certificate  """  
      self.TaxNumberType:str = obj["TaxNumberType"]
      """  The tax number type for the certificate. For example, FEIN, Social Security Number, or Employer Identification Number.  """  
      self.Valid:bool = obj["Valid"]
      """  True if this certificate is marked as valid. A valid certificate can be considered for exemption purposes. When a certificate is marked invalid, it will no longer be considered when calculating exemption for a customer.  """  
      self.ValidatedExemptReason:str = obj["ValidatedExemptReason"]
      """  The exemption reason that CertCapture audit/internal logic identifies for created certificate.  """  
      self.Verified:bool = obj["Verified"]
      """  This value is true if the certificate has gone through the certificate validation process.  """  
      self.SingleUse:bool = obj["SingleUse"]
      """  Is this document limited to one document/order/invoice?  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxConnectCertificatesTableset:
   def __init__(self, obj):
      self.TaxConnectCertificates:list[Erp_Tablesets_TaxConnectCertificatesRow] = obj["TaxConnectCertificates"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetTaxConnectCertificates_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      pass

class GetTaxConnectCertificates_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxConnectCertificatesTableset] = obj["returnObj"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class RequestTaxConnectCertificateCustomerInvite_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      pass

class RequestTaxConnectCertificateCustomerInvite_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message if invite link was generated/sent successfully  """  
      pass

class SendCustomerToTaxConnect_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      pass

class SendCustomerToTaxConnect_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message if upload was successful  """  
      pass

