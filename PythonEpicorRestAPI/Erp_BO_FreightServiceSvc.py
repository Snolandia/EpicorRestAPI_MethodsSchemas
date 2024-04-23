import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FreightServiceSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_BuildCustFreightRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildCustFreightRequest
   Description: Build the customer freight request
   OperationID: BuildCustFreightRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCustFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCustFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateTimeOut(epicorHeaders = None):
   """  
   Summary: Invoke method UpdateTimeOut
   Description: UpdateTimeOut in http calls
   OperationID: UpdateTimeOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateTimeOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_LogManifestMsg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LogManifestMsg
   Description: Create Manifest Log File
   OperationID: LogManifestMsg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LogManifestMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LogManifestMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildGenUnfreightManifest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildGenUnfreightManifest
   Description: UnFreigth Manifest
   OperationID: BuildGenUnfreightManifest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildGenUnfreightManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildGenUnfreightManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildMasterPackFreightRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildMasterPackFreightRequest
   Description: Build the freight request based upon the masterpack
   OperationID: BuildMasterPackFreightRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildMasterPackFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildMasterPackFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildMiscFreightRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildMiscFreightRequest
   Description: build the miscellaneous shipment freight request
   OperationID: BuildMiscFreightRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildMiscFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildMiscFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildSubFreightRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildSubFreightRequest
   Description: build the subcontract freight request
   OperationID: BuildSubFreightRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildSubFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildSubFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildTransFreightRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildTransFreightRequest
   Description: build the transfer freight request
   OperationID: BuildTransFreightRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildTransFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildTransFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateFreightedShipment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateFreightedShipment
   Description: Update the freighted shipment
   OperationID: UpdateFreightedShipment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateFreightedShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFreightedShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateUnFreightedShipment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateUnFreightedShipment
   Description: Unfreight a shipment
   OperationID: UpdateUnFreightedShipment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateUnFreightedShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateUnFreightedShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FreightCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FreightCarton
   Description: Call for Manifest Freight Carton
   OperationID: FreightCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FreightCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FreightCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnfreightCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnfreightCarton
   Description: Call for Manifest Unfreight Carton
   OperationID: UnfreightCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnfreightCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnfreightCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildCustFreightRequest_input:
   """ Required : 
   packID
   """  
   def __init__(self, obj):
      self.packID:int = obj["packID"]
      """  Pack Number  """  
      pass

class BuildCustFreightRequest_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FreightInfoRequestTableset] = obj["returnObj"]
      pass

class BuildGenUnfreightManifest_input:
   """ Required : 
   userID
   packID
   packType
   cartonRequest
   WorkStationID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  userID  """  
      self.packID:int = obj["packID"]
      """  packID  """  
      self.packType:str = obj["packType"]
      """  packType  """  
      self.cartonRequest      #schema had no properties on an object.
      """  cartonRequest  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  WorkStationID  """  
      pass

class BuildGenUnfreightManifest_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class BuildMasterPackFreightRequest_input:
   """ Required : 
   packID
   """  
   def __init__(self, obj):
      self.packID:int = obj["packID"]
      """  Pack Number  """  
      pass

class BuildMasterPackFreightRequest_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FreightInfoRequestTableset] = obj["returnObj"]
      pass

class BuildMiscFreightRequest_input:
   """ Required : 
   packID
   """  
   def __init__(self, obj):
      self.packID:int = obj["packID"]
      """  Pack Number  """  
      pass

class BuildMiscFreightRequest_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FreightInfoRequestTableset] = obj["returnObj"]
      pass

class BuildSubFreightRequest_input:
   """ Required : 
   packID
   """  
   def __init__(self, obj):
      self.packID:int = obj["packID"]
      """  Pack Number  """  
      pass

class BuildSubFreightRequest_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FreightInfoRequestTableset] = obj["returnObj"]
      pass

class BuildTransFreightRequest_input:
   """ Required : 
   packID
   """  
   def __init__(self, obj):
      self.packID:int = obj["packID"]
      """  Pack Number  """  
      pass

class BuildTransFreightRequest_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FreightInfoRequestTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_COORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MasterpackPackID:int = obj["MasterpackPackID"]
      self.PackID:int = obj["PackID"]
      self.OrderNum:str = obj["OrderNum"]
      self.OrderLineNum:int = obj["OrderLineNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.OrigCountry:int = obj["OrigCountry"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.PartNum:str = obj["PartNum"]
      self.QtyPerc:int = obj["QtyPerc"]
      self.ValuePerc:int = obj["ValuePerc"]
      self.Primary:bool = obj["Primary"]
      self.RelatedToFile:str = obj["RelatedToFile"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FreightCartonResponseRow:
   def __init__(self, obj):
      self.CallTagNumber:str = obj["CallTagNumber"]
      self.DimWeight:int = obj["DimWeight"]
      self.DimWeightUOM:str = obj["DimWeightUOM"]
      self.DiscountFreightAmount:int = obj["DiscountFreightAmount"]
      self.DiscountFreightAmountUOM:str = obj["DiscountFreightAmountUOM"]
      self.ErrorFlag:bool = obj["ErrorFlag"]
      self.ErrorMessage:str = obj["ErrorMessage"]
      self.EstimatedFreightAmount:int = obj["EstimatedFreightAmount"]
      self.EstimatedFreightAmountUOM:str = obj["EstimatedFreightAmountUOM"]
      self.EstimatedFreightFlag:bool = obj["EstimatedFreightFlag"]
      self.FreightZone:str = obj["FreightZone"]
      self.OtherAmount:int = obj["OtherAmount"]
      self.OtherAmountUOM:str = obj["OtherAmountUOM"]
      self.OversizeFlag:bool = obj["OversizeFlag"]
      self.PickupNumber:str = obj["PickupNumber"]
      self.PublishedFreightAmount:int = obj["PublishedFreightAmount"]
      self.PublishedFreightAmountUOM:str = obj["PublishedFreightAmountUOM"]
      self.ShipDate:str = obj["ShipDate"]
      self.TemplateCode:str = obj["TemplateCode"]
      self.TransactionNumber:str = obj["TransactionNumber"]
      self.WayBillNbr:str = obj["WayBillNbr"]
      self.FreightedShipVia:str = obj["FreightedShipVia"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FreightCartonResponseTrackingRow:
   def __init__(self, obj):
      self.TrackingNumber:str = obj["TrackingNumber"]
      self.PackID:int = obj["PackID"]
      self.DiscountFreightAmt:int = obj["DiscountFreightAmt"]
      """  Discounted freight amount calculated by the shipper  """  
      self.PublishedFreightAmt:int = obj["PublishedFreightAmt"]
      """  Published freight amount determined by the shipper.  """  
      self.CaseNum:str = obj["CaseNum"]
      """  Concatenation of the pack num and sequential case number.  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Shipment type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FreightInfoRequestTableset:
   def __init__(self, obj):
      self.MasterPackInfo:list[Erp_Tablesets_MasterPackInfoRow] = obj["MasterPackInfo"]
      self.PackInfo:list[Erp_Tablesets_PackInfoRow] = obj["PackInfo"]
      self.OrderInfo:list[Erp_Tablesets_OrderInfoRow] = obj["OrderInfo"]
      self.OrderLine:list[Erp_Tablesets_OrderLineRow] = obj["OrderLine"]
      self.COO:list[Erp_Tablesets_COORow] = obj["COO"]
      self.KitComponent:list[Erp_Tablesets_KitComponentRow] = obj["KitComponent"]
      self.PhantomPack:list[Erp_Tablesets_PhantomPackRow] = obj["PhantomPack"]
      self.UPSQV:list[Erp_Tablesets_UPSQVRow] = obj["UPSQV"]
      self.MasterUPSQV:list[Erp_Tablesets_MasterUPSQVRow] = obj["MasterUPSQV"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FreightInfoResponseTableset:
   def __init__(self, obj):
      self.FreightCartonResponse:list[Erp_Tablesets_FreightCartonResponseRow] = obj["FreightCartonResponse"]
      self.FreightCartonResponseTracking:list[Erp_Tablesets_FreightCartonResponseTrackingRow] = obj["FreightCartonResponseTracking"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_KitComponentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MasterpackPackID:int = obj["MasterpackPackID"]
      self.PackID:int = obj["PackID"]
      self.OrderNum:str = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.AESExp:str = obj["AESExp"]
      self.ECNNumber:str = obj["ECNNumber"]
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      self.ExpLicType:str = obj["ExpLicType"]
      self.HazClass:str = obj["HazClass"]
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      self.HazItem:bool = obj["HazItem"]
      self.HazPackInstr:str = obj["HazPackInstr"]
      self.HazSub:str = obj["HazSub"]
      self.HazTechName:str = obj["HazTechName"]
      self.HTS:str = obj["HTS"]
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      self.NAFTAPref:str = obj["NAFTAPref"]
      self.NAFTAProd:str = obj["NAFTAProd"]
      self.OrigCountry:str = obj["OrigCountry"]
      self.SchedBcode:str = obj["SchedBcode"]
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      self.PartDescription:str = obj["PartDescription"]
      self.QtyShip:int = obj["QtyShip"]
      self.QtyShipUOM:str = obj["QtyShipUOM"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.Date20:str = obj["Date20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.KitParentLine:int = obj["KitParentLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackInfoRow:
   def __init__(self, obj):
      self.AddFreightToAmountFlag:bool = obj["AddFreightToAmountFlag"]
      self.AODFlag:bool = obj["AODFlag"]
      self.AutoPODFlag:bool = obj["AutoPODFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.ContentValue:int = obj["ContentValue"]
      self.DeclaredValue:int = obj["DeclaredValue"]
      self.DeclaredValueCurrencyUOM:str = obj["DeclaredValueCurrencyUOM"]
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      self.DocumentsOnlyFlag:bool = obj["DocumentsOnlyFlag"]
      self.EmailNotificationAddresses:str = obj["EmailNotificationAddresses"]
      self.EmailNotificationFlag:bool = obj["EmailNotificationFlag"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.FreightCarrier:str = obj["FreightCarrier"]
      self.FreightType:str = obj["FreightType"]
      self.GroundCollectionTypeCode:str = obj["GroundCollectionTypeCode"]
      self.HandlingCharge:int = obj["HandlingCharge"]
      self.HandlingChargeCurrencyUOM:str = obj["HandlingChargeCurrencyUOM"]
      self.HandlingChargeFlag:bool = obj["HandlingChargeFlag"]
      self.HazardousShipment:bool = obj["HazardousShipment"]
      self.Height:int = obj["Height"]
      self.HeightUOM:str = obj["HeightUOM"]
      self.HomeDeliveryDate:str = obj["HomeDeliveryDate"]
      self.HomeDeliveryFlag:bool = obj["HomeDeliveryFlag"]
      self.HomeDeliveryInstr:str = obj["HomeDeliveryInstr"]
      self.HomeDeliveryPhone:str = obj["HomeDeliveryPhone"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.Length:int = obj["Length"]
      self.LengthUOM:str = obj["LengthUOM"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.MoneyOrderAmount:int = obj["MoneyOrderAmount"]
      self.MoneyOrderAmountCurrUOM:str = obj["MoneyOrderAmountCurrUOM"]
      self.MoneyOrderRequiredFlag:bool = obj["MoneyOrderRequiredFlag"]
      self.PackID:int = obj["PackID"]
      self.PayAccount:str = obj["PayAccount"]
      self.PayBTCity:str = obj["PayBTCity"]
      self.PayBTCountry:str = obj["PayBTCountry"]
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      self.PayBTState:str = obj["PayBTState"]
      self.PayFlag:str = obj["PayFlag"]
      self.PriorityAlertFlag:bool = obj["PriorityAlertFlag"]
      self.Reference1:str = obj["Reference1"]
      self.Reference2:str = obj["Reference2"]
      self.Reference3:str = obj["Reference3"]
      self.Reference4:str = obj["Reference4"]
      self.Reference5:str = obj["Reference5"]
      self.ReferenceNotes:str = obj["ReferenceNotes"]
      self.ReleaseAuthNumber:str = obj["ReleaseAuthNumber"]
      self.ReleaseOnFileFlag:bool = obj["ReleaseOnFileFlag"]
      self.ResidentialDeliveryFlag:bool = obj["ResidentialDeliveryFlag"]
      self.SaturdayDeliveryFlag:bool = obj["SaturdayDeliveryFlag"]
      self.SaturdayPickupFlag:bool = obj["SaturdayPickupFlag"]
      self.SequenceNum:int = obj["SequenceNum"]
      self.ServiceSaturdayDeliveryFlag:bool = obj["ServiceSaturdayDeliveryFlag"]
      self.ServiceSaturdayPickupFlag:bool = obj["ServiceSaturdayPickupFlag"]
      self.ShipDate:str = obj["ShipDate"]
      self.ShipExportDeclartn:bool = obj["ShipExportDeclartn"]
      self.ShipToAddress:str = obj["ShipToAddress"]
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      self.ShipToAttention:str = obj["ShipToAttention"]
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToFax:str = obj["ShipToFax"]
      self.ShipToID:str = obj["ShipToID"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToPhone:str = obj["ShipToPhone"]
      self.ShipToPostalCode:str = obj["ShipToPostalCode"]
      self.ShipToRegion:str = obj["ShipToRegion"]
      self.ShipToTerritory:str = obj["ShipToTerritory"]
      self.SignatureRequiredFlag:bool = obj["SignatureRequiredFlag"]
      self.SoldToAddress:str = obj["SoldToAddress"]
      self.SoldToAddress2:str = obj["SoldToAddress2"]
      self.SoldToAttention:str = obj["SoldToAttention"]
      self.SoldToCity:str = obj["SoldToCity"]
      self.SoldToCountry:str = obj["SoldToCountry"]
      self.SoldToFax:str = obj["SoldToFax"]
      self.SoldToID:str = obj["SoldToID"]
      self.SoldToName:str = obj["SoldToName"]
      self.SoldToPhone:str = obj["SoldToPhone"]
      self.SoldToPostalCode:str = obj["SoldToPostalCode"]
      self.SoldToRegion:str = obj["SoldToRegion"]
      self.SoldToTerritory:str = obj["SoldToTerritory"]
      self.StationID:str = obj["StationID"]
      self.TemplateCode:str = obj["TemplateCode"]
      self.VerbalConfirmationFlag:bool = obj["VerbalConfirmationFlag"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.Width:int = obj["Width"]
      self.WidthUOM:str = obj["WidthUOM"]
      self.PackIDList:str = obj["PackIDList"]
      self.UserEntryID:str = obj["UserEntryID"]
      self.PayBTZip:str = obj["PayBTZip"]
      """  Pay Zip Code  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Misc, Customer, SubContract or Transfer  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      self.SoldToAddress3:str = obj["SoldToAddress3"]
      """  Sold To Address 3  """  
      self.IndividualPackIds:bool = obj["IndividualPackIds"]
      self.ServSignature:bool = obj["ServSignature"]
      self.DeliveryConf:int = obj["DeliveryConf"]
      """  Determines the level of delivery confirmation.   1 - No Signature Required 2 - Adult Signature Required 3 - Confirmation Required 4 - Verbal Confirmation Required  """  
      self.FFAddress3:str = obj["FFAddress3"]
      self.NonStdPkg:bool = obj["NonStdPkg"]
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      self.PayBTPhone:str = obj["PayBTPhone"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.PkgCode:str = obj["PkgCode"]
      """  Package code  """  
      self.ManifestType:str = obj["ManifestType"]
      """  Identifies the type of manifest the third party shipping applications are to process.  SPack is a standard pack, MPack is a master pack, PPack is a Phantom Pack and MPIND is an individual master pack.  """  
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.SoldToUseBlindShipping:bool = obj["SoldToUseBlindShipping"]
      self.CustomerNotes:str = obj["CustomerNotes"]
      self.ShipperNotes:str = obj["ShipperNotes"]
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      self.LabelComment:str = obj["LabelComment"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterUPSQVRow:
   def __init__(self, obj):
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVEmailAddrs:str = obj["UPSQVEmailAddrs"]
      self.UPSQVShipNotList:bool = obj["UPSQVShipNotList"]
      self.UPSQVExceptNotList:bool = obj["UPSQVExceptNotList"]
      self.UPSQVDelNotList:bool = obj["UPSQVDelNotList"]
      self.Company:str = obj["Company"]
      self.PackID:int = obj["PackID"]
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Character11:str = obj["Character11"]
      self.Character12:str = obj["Character12"]
      self.Character13:str = obj["Character13"]
      self.Character14:str = obj["Character14"]
      self.Character15:str = obj["Character15"]
      self.Character16:str = obj["Character16"]
      self.Character17:str = obj["Character17"]
      self.Character18:str = obj["Character18"]
      self.Character19:str = obj["Character19"]
      self.Character20:str = obj["Character20"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderInfoRow:
   def __init__(self, obj):
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.CustPONumber:str = obj["CustPONumber"]
      self.DropShip:bool = obj["DropShip"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.JobNumber:str = obj["JobNumber"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.OrderNum:str = obj["OrderNum"]
      self.PayAccount:str = obj["PayAccount"]
      self.PayBTCity:str = obj["PayBTCity"]
      self.PayBTCountry:str = obj["PayBTCountry"]
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      self.PayBTState:str = obj["PayBTState"]
      self.PayBTZip:str = obj["PayBTZip"]
      self.PayFlag:str = obj["PayFlag"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      self.TotalOrderValueCurrencyUOM:str = obj["TotalOrderValueCurrencyUOM"]
      self.OrderType:str = obj["OrderType"]
      self.PartList:str = obj["PartList"]
      self.CustID:str = obj["CustID"]
      """  Customer  """  
      self.PayBTName:str = obj["PayBTName"]
      """  Pay Bill To Name  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Billing address3  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forward Address 3  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Billing phone number  """  
      self.Company:str = obj["Company"]
      self.MasterpackPackID:int = obj["MasterpackPackID"]
      self.PackID:int = obj["PackID"]
      self.PackslipComments:str = obj["PackslipComments"]
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.DeliveryInstr:str = obj["DeliveryInstr"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderLineRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MasterpackPackID:int = obj["MasterpackPackID"]
      self.PackID:int = obj["PackID"]
      self.OrderNum:str = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.QTYShipUOM:str = obj["QTYShipUOM"]
      self.Kit:bool = obj["Kit"]
      self.KitPrintCompPack:bool = obj["KitPrintCompPack"]
      self.KitPrintCompCust:bool = obj["KitPrintCompCust"]
      self.AESExp:str = obj["AESExp"]
      self.ECNNumber:str = obj["ECNNumber"]
      self.ExpLicType:str = obj["ExpLicType"]
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      self.HazClass:str = obj["HazClass"]
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      self.HazItem:bool = obj["HazItem"]
      self.HazPackInstr:str = obj["HazPackInstr"]
      self.HazSub:str = obj["HazSub"]
      self.HazTechName:str = obj["HazTechName"]
      self.HTS:str = obj["HTS"]
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      self.NAFTAPref:str = obj["NAFTAPref"]
      self.NAFTAProd:str = obj["NAFTAProd"]
      self.OrigCountry:str = obj["OrigCountry"]
      self.SchedBcode:str = obj["SchedBcode"]
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.QtyShip:int = obj["QtyShip"]
      self.OrderLineNum:int = obj["OrderLineNum"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.PartCharacter01:str = obj["PartCharacter01"]
      self.PartCharacter02:str = obj["PartCharacter02"]
      self.PartCharacter03:str = obj["PartCharacter03"]
      self.PartCharacter04:str = obj["PartCharacter04"]
      self.PartCharacter05:str = obj["PartCharacter05"]
      self.PartCharacter06:str = obj["PartCharacter06"]
      self.PartCharacter07:str = obj["PartCharacter07"]
      self.PartCharacter08:str = obj["PartCharacter08"]
      self.PartCharacter09:str = obj["PartCharacter09"]
      self.PartCharacter10:str = obj["PartCharacter10"]
      self.PartCheckBox01:bool = obj["PartCheckBox01"]
      self.PartCheckBox02:bool = obj["PartCheckBox02"]
      self.PartCheckBox03:bool = obj["PartCheckBox03"]
      self.PartCheckBox04:bool = obj["PartCheckBox04"]
      self.PartCheckBox05:bool = obj["PartCheckBox05"]
      self.PartCheckBox06:bool = obj["PartCheckBox06"]
      self.PartCheckBox07:bool = obj["PartCheckBox07"]
      self.PartCheckBox08:bool = obj["PartCheckBox08"]
      self.PartCheckBox09:bool = obj["PartCheckBox09"]
      self.PartCheckBox10:bool = obj["PartCheckBox10"]
      self.PartCheckBox11:bool = obj["PartCheckBox11"]
      self.PartCheckBox12:bool = obj["PartCheckBox12"]
      self.PartCheckBox13:bool = obj["PartCheckBox13"]
      self.PartCheckBox14:bool = obj["PartCheckBox14"]
      self.PartCheckBox15:bool = obj["PartCheckBox15"]
      self.PartCheckBox16:bool = obj["PartCheckBox16"]
      self.PartCheckBox17:bool = obj["PartCheckBox17"]
      self.PartCheckBox18:bool = obj["PartCheckBox18"]
      self.PartCheckBox19:bool = obj["PartCheckBox19"]
      self.PartCheckBox20:bool = obj["PartCheckBox20"]
      self.PartDate01:str = obj["PartDate01"]
      self.PartDate02:str = obj["PartDate02"]
      self.PartDate03:str = obj["PartDate03"]
      self.PartDate04:str = obj["PartDate04"]
      self.PartDate05:str = obj["PartDate05"]
      self.PartDate06:str = obj["PartDate06"]
      self.PartDate07:str = obj["PartDate07"]
      self.PartDate08:str = obj["PartDate08"]
      self.PartDate09:str = obj["PartDate09"]
      self.PartDate10:str = obj["PartDate10"]
      self.PartDate11:str = obj["PartDate11"]
      self.PartDate12:str = obj["PartDate12"]
      self.PartDate13:str = obj["PartDate13"]
      self.PartDate14:str = obj["PartDate14"]
      self.PartDate15:str = obj["PartDate15"]
      self.PartDate16:str = obj["PartDate16"]
      self.PartDate17:str = obj["PartDate17"]
      self.PartDate18:str = obj["PartDate18"]
      self.PartDate19:str = obj["PartDate19"]
      self.PartDate20:str = obj["PartDate20"]
      self.PartNumber01:int = obj["PartNumber01"]
      self.PartNumber02:int = obj["PartNumber02"]
      self.PartNumber03:int = obj["PartNumber03"]
      self.PartNumber04:int = obj["PartNumber04"]
      self.PartNumber05:int = obj["PartNumber05"]
      self.PartNumber06:int = obj["PartNumber06"]
      self.PartNumber07:int = obj["PartNumber07"]
      self.PartNumber08:int = obj["PartNumber08"]
      self.PartNumber09:int = obj["PartNumber09"]
      self.PartNumber10:int = obj["PartNumber10"]
      self.PartNumber11:int = obj["PartNumber11"]
      self.PartNumber12:int = obj["PartNumber12"]
      self.PartNumber13:int = obj["PartNumber13"]
      self.PartNumber14:int = obj["PartNumber14"]
      self.PartNumber15:int = obj["PartNumber15"]
      self.PartNumber16:int = obj["PartNumber16"]
      self.PartNumber17:int = obj["PartNumber17"]
      self.PartNumber18:int = obj["PartNumber18"]
      self.PartNumber19:int = obj["PartNumber19"]
      self.PartNumber20:int = obj["PartNumber20"]
      self.PartShortChar01:str = obj["PartShortChar01"]
      self.PartShortChar02:str = obj["PartShortChar02"]
      self.PartShortChar03:str = obj["PartShortChar03"]
      self.PartShortChar04:str = obj["PartShortChar04"]
      self.PartShortChar05:str = obj["PartShortChar05"]
      self.PartShortChar06:str = obj["PartShortChar06"]
      self.PartShortChar07:str = obj["PartShortChar07"]
      self.PartShortChar08:str = obj["PartShortChar08"]
      self.PartShortChar09:str = obj["PartShortChar09"]
      self.PartShortChar10:str = obj["PartShortChar10"]
      self.BOLClass:str = obj["BOLClass"]
      """  Bill of Landing Class. Additional data for the part required for LTL and International shipments.  """  
      self.FairMarketValue:int = obj["FairMarketValue"]
      """  Fair Market Value. Additional data for the part required for LTL and International shipments.  """  
      self.NetWeight:int = obj["NetWeight"]
      """  The Part's Unit Net Weight.  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """   Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  The Part's Unit Gross Weight.  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   The Part's Unit Gross Weight. 
Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight". Use UOMClass.DefUOMCode of the "weight" UOMClass as a default when creating new part records.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackInfoRow:
   def __init__(self, obj):
      self.AddFreightToAmountFlag:bool = obj["AddFreightToAmountFlag"]
      self.AODFlag:bool = obj["AODFlag"]
      self.AutoPODflag:bool = obj["AutoPODflag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.ContentValue:int = obj["ContentValue"]
      self.ContentValueCurrencyUOM:str = obj["ContentValueCurrencyUOM"]
      self.ConZip:str = obj["ConZip"]
      self.DeclaredValue:int = obj["DeclaredValue"]
      self.DeclaredValueCurrencyUOM:str = obj["DeclaredValueCurrencyUOM"]
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      self.DocumentsOnlyFlag:bool = obj["DocumentsOnlyFlag"]
      self.EmailNotificationAddresses:str = obj["EmailNotificationAddresses"]
      self.EmailNotificationFlag:bool = obj["EmailNotificationFlag"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      """  `  """  
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.FreightCarrier:str = obj["FreightCarrier"]
      self.FreightType:str = obj["FreightType"]
      self.GroundCollectionTypeCode:str = obj["GroundCollectionTypeCode"]
      self.HandlingCharge:int = obj["HandlingCharge"]
      self.HandlingChargeCurrencyUOM:str = obj["HandlingChargeCurrencyUOM"]
      self.HandlingChargeFlag:bool = obj["HandlingChargeFlag"]
      self.HazardousShipment:bool = obj["HazardousShipment"]
      self.HeightUOM:str = obj["HeightUOM"]
      self.HomeDeliveryDate:str = obj["HomeDeliveryDate"]
      self.HomeDeliveryFlag:bool = obj["HomeDeliveryFlag"]
      self.HomeDeliveryInstr:str = obj["HomeDeliveryInstr"]
      self.HomeDeliveryPhone:str = obj["HomeDeliveryPhone"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.Length:int = obj["Length"]
      self.LengthUOM:str = obj["LengthUOM"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.MoneyOrderAmount:int = obj["MoneyOrderAmount"]
      self.MoneyOrderAmountCurrUOM:str = obj["MoneyOrderAmountCurrUOM"]
      self.MoneyOrderRequiredFlag:bool = obj["MoneyOrderRequiredFlag"]
      self.PackID:int = obj["PackID"]
      self.PayAccount:str = obj["PayAccount"]
      self.PayBTCity:str = obj["PayBTCity"]
      self.PayBTCountry:str = obj["PayBTCountry"]
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      self.PayBTState:str = obj["PayBTState"]
      self.PayFlag:str = obj["PayFlag"]
      self.PriorityAlertFlag:bool = obj["PriorityAlertFlag"]
      self.Reference1:str = obj["Reference1"]
      self.Reference2:str = obj["Reference2"]
      self.Reference3:str = obj["Reference3"]
      self.Reference4:str = obj["Reference4"]
      self.Reference5:str = obj["Reference5"]
      self.ReferenceNotes:str = obj["ReferenceNotes"]
      self.ReleaseAuthNumber:str = obj["ReleaseAuthNumber"]
      self.ReleaseOnFileFlag:bool = obj["ReleaseOnFileFlag"]
      self.ResidentialDeliveryFlag:bool = obj["ResidentialDeliveryFlag"]
      self.SaturdayDeliveryFlag:bool = obj["SaturdayDeliveryFlag"]
      self.SaturdayPickupFlag:bool = obj["SaturdayPickupFlag"]
      self.SequenceNum:int = obj["SequenceNum"]
      self.ServiceSaturdayDeliveryFlag:bool = obj["ServiceSaturdayDeliveryFlag"]
      self.ServiceSaturdayPickupFlag:bool = obj["ServiceSaturdayPickupFlag"]
      self.ShipDate:str = obj["ShipDate"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.ShipToAddress:str = obj["ShipToAddress"]
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      self.ShipToAttention:str = obj["ShipToAttention"]
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToFax:str = obj["ShipToFax"]
      self.ShipToID:str = obj["ShipToID"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToPhone:str = obj["ShipToPhone"]
      self.ShipToPostalCode:str = obj["ShipToPostalCode"]
      self.ShipToRegion:str = obj["ShipToRegion"]
      self.ShipToTerritory:str = obj["ShipToTerritory"]
      self.SignatureRequiredFlag:bool = obj["SignatureRequiredFlag"]
      self.SoldToAddress:str = obj["SoldToAddress"]
      self.SoldToAddress2:str = obj["SoldToAddress2"]
      self.SoldToAttention:str = obj["SoldToAttention"]
      self.SoldToCity:str = obj["SoldToCity"]
      self.SoldToCountry:str = obj["SoldToCountry"]
      self.SoldToFax:str = obj["SoldToFax"]
      self.SoldToID:str = obj["SoldToID"]
      self.SoldToName:str = obj["SoldToName"]
      self.SoldToPhone:str = obj["SoldToPhone"]
      self.SoldToPostalCode:str = obj["SoldToPostalCode"]
      self.SoldToRegion:str = obj["SoldToRegion"]
      self.SoldToTerritory:str = obj["SoldToTerritory"]
      self.StationID:str = obj["StationID"]
      self.TemplateCode:str = obj["TemplateCode"]
      self.VerbalConfirmationFlag:bool = obj["VerbalConfirmationFlag"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.Width:int = obj["Width"]
      self.WidthUOM:str = obj["WidthUOM"]
      self.OrderList:str = obj["OrderList"]
      self.UserEntryID:str = obj["UserEntryID"]
      self.PayBTZip:str = obj["PayBTZip"]
      self.Height:int = obj["Height"]
      """  Height  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Transfer, Customer, Subcontract or Misc  """  
      self.SoldToAddress3:str = obj["SoldToAddress3"]
      """  Sold To Address 3  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      """  Ship To Address 3  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forward Address line 3  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Billing phone number  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Bililng address line 3  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  logical indicating if the packaing is standard  """  
      self.PkgCode:str = obj["PkgCode"]
      """  packaging  """  
      self.CaseNum:str = obj["CaseNum"]
      """  Vantage generated case number sent to third party shipping packages.  Concatenation of the PackNum and a sequential counter.  """  
      self.MasterpackPackID:int = obj["MasterpackPackID"]
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.SoldToUseBlindShipping:bool = obj["SoldToUseBlindShipping"]
      self.IncotermCode:str = obj["IncotermCode"]
      self.IncotermLocation:str = obj["IncotermLocation"]
      self.CustomerNotes:str = obj["CustomerNotes"]
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      self.LabelComment:str = obj["LabelComment"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PhantomPackRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MasterpackPackID:int = obj["MasterpackPackID"]
      self.PackID:int = obj["PackID"]
      self.CaseNumber:str = obj["CaseNumber"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.Length:int = obj["Length"]
      self.LengthUOM:str = obj["LengthUOM"]
      self.Width:int = obj["Width"]
      self.WidthUOM:str = obj["WidthUOM"]
      self.Height:int = obj["Height"]
      self.HeightUOM:str = obj["HeightUOM"]
      self.CODAmount:int = obj["CODAmount"]
      self.DeclaredValue:bool = obj["DeclaredValue"]
      self.DeclaredAmount:int = obj["DeclaredAmount"]
      self.CheckMOReq:bool = obj["CheckMOReq"]
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UPSQVRow:
   def __init__(self, obj):
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVEmailAddrs:str = obj["UPSQVEmailAddrs"]
      self.UPSQVShipNotList:bool = obj["UPSQVShipNotList"]
      self.UPSQVExceptNotList:bool = obj["UPSQVExceptNotList"]
      self.UPSQVDelNotList:bool = obj["UPSQVDelNotList"]
      self.Company:str = obj["Company"]
      self.MasterpackPackID:int = obj["MasterpackPackID"]
      self.PackID:int = obj["PackID"]
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Character11:str = obj["Character11"]
      self.Character12:str = obj["Character12"]
      self.Character13:str = obj["Character13"]
      self.Character14:str = obj["Character14"]
      self.Character15:str = obj["Character15"]
      self.Character16:str = obj["Character16"]
      self.Character17:str = obj["Character17"]
      self.Character18:str = obj["Character18"]
      self.Character19:str = obj["Character19"]
      self.Character20:str = obj["Character20"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UnfreightCartonResponseRow:
   def __init__(self, obj):
      self.PackID:int = obj["PackID"]
      self.ErrorFlag:bool = obj["ErrorFlag"]
      self.ErrorMessage:str = obj["ErrorMessage"]
      self.UnfreightDate:str = obj["UnfreightDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UnfreightInfoResponseTableset:
   def __init__(self, obj):
      self.UnfreightCartonResponse:list[Erp_Tablesets_UnfreightCartonResponseRow] = obj["UnfreightCartonResponse"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FreightCarton_input:
   """ Required : 
   freightURL
   rdt
   WorkStationID
   httpTimeOut
   """  
   def __init__(self, obj):
      self.freightURL:str = obj["freightURL"]
      self.rdt      #schema had no properties on an object.
      self.WorkStationID:str = obj["WorkStationID"]
      self.httpTimeOut:int = obj["httpTimeOut"]
      pass

class FreightCarton_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
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

class LogManifestMsg_input:
   """ Required : 
   tds
   rds
   packNum
   shipmentType
   """  
   def __init__(self, obj):
      self.tds:list[Erp_Tablesets_FreightInfoRequestTableset] = obj["tds"]
      self.rds:list[Erp_Tablesets_FreightInfoResponseTableset] = obj["rds"]
      self.packNum:int = obj["packNum"]
      """  packNum  """  
      self.shipmentType:str = obj["shipmentType"]
      """  shipmentType  """  
      pass

class LogManifestMsg_output:
   def __init__(self, obj):
      pass

class UnfreightCarton_input:
   """ Required : 
   freightURL
   urds
   WorkStationID
   httpTimeOut
   """  
   def __init__(self, obj):
      self.freightURL:str = obj["freightURL"]
      self.urds      #schema had no properties on an object.
      self.WorkStationID:str = obj["WorkStationID"]
      self.httpTimeOut:int = obj["httpTimeOut"]
      pass

class UnfreightCarton_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class UpdateFreightedShipment_input:
   """ Required : 
   ipPackID
   ipShipmentType
   ds
   """  
   def __init__(self, obj):
      self.ipPackID:int = obj["ipPackID"]
      """  package code  """  
      self.ipShipmentType:str = obj["ipShipmentType"]
      """  shipment type  """  
      self.ds:list[Erp_Tablesets_FreightInfoResponseTableset] = obj["ds"]
      pass

class UpdateFreightedShipment_output:
   def __init__(self, obj):
      pass

class UpdateTimeOut_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.httpTimeOut:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateUnFreightedShipment_input:
   """ Required : 
   ipPackID
   ipShipmentType
   ds
   """  
   def __init__(self, obj):
      self.ipPackID:int = obj["ipPackID"]
      """  package code  """  
      self.ipShipmentType:str = obj["ipShipmentType"]
      """  shipment type  """  
      self.ds:list[Erp_Tablesets_UnfreightInfoResponseTableset] = obj["ds"]
      pass

class UpdateUnFreightedShipment_output:
   def __init__(self, obj):
      pass

