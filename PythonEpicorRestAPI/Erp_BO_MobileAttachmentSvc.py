import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MobileAttachmentSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetDocumentTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDocumentTypes
   Description: Retrieve document types  valid for
   OperationID: GetDocumentTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDocumentTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDocumentTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVersion(epicorHeaders = None):
   """  
   Summary: Invoke method GetVersion
   Description: Returns BO Version
   OperationID: GetVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_MobileAttachmentTableset:
   def __init__(self, obj):
      self.MobileXFileAttch:list[Erp_Tablesets_MobileXFileAttchRow] = obj["MobileXFileAttch"]
      self.MobileDocType:list[Erp_Tablesets_MobileDocTypeRow] = obj["MobileDocType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MobileDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """   Unique identifier of a DocType. Assigned by the user.
Cannot be blank.  """  
      self.Description:str = obj["Description"]
      """  Full description of the DocType.  """  
      self.Receipt:bool = obj["Receipt"]
      """   Indicates if the document type is one that would fullfill the rule that receipt documents be attached for inventory receipts of a Part Lot for a Part that has Part.RecDocReq = Yes  Defaults as No.
These required documents are duplicate from the receipt detail to the part lot.  """  
      self.Shipment:bool = obj["Shipment"]
      """   Indicates if the document type is one that would fullfill the rule that shipping documents be attached before allowing the user
to set the ShipDocAvail flag on the PartLot or Job. (See Part.ShipDocAvail)  """  
      self.BaseURL:str = obj["BaseURL"]
      """  Optional. But if given, used as intial default to the attachement filename field. Note this is expressed in the CLient OS format (MS Windows). Usually using  UNC naming convention or common mapped drive  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.StorageType:int = obj["StorageType"]
      """  Storage Type  """  
      self.ImageName:str = obj["ImageName"]
      """  Image Name  """  
      self.SpecificTables:bool = obj["SpecificTables"]
      """  Specific Tables  """  
      self.GlobalDocType:bool = obj["GlobalDocType"]
      """  Marks this DocType as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FileTransferMode:int = obj["FileTransferMode"]
      """  FileTransferMode  """  
      self.AuthType:str = obj["AuthType"]
      """  AuthType  """  
      self.DirectoryID:str = obj["DirectoryID"]
      """  DirectoryID  """  
      self.ApplicationID:str = obj["ApplicationID"]
      """  ApplicationID  """  
      self.CertificateThumbPrint:str = obj["CertificateThumbPrint"]
      """  CertificateThumbPrint  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileXFileAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  """  
      self.AttachNum:int = obj["AttachNum"]
      """   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  """  
      self.XFileRefNum:int = obj["XFileRefNum"]
      """  Foreign Key to XFileRef record.  """  
      self.DoTrigger:bool = obj["DoTrigger"]
      """  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  """  
      self.DupToRelatedToFile:str = obj["DupToRelatedToFile"]
      """  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  """  
      self.DupToKey1:str = obj["DupToKey1"]
      """  See DupToRelatedToFile  """  
      self.DupToKey2:str = obj["DupToKey2"]
      """  See DupToRelatedToFile  """  
      self.DupToKey3:str = obj["DupToKey3"]
      """  See DupToRelatedToFile  """  
      self.DupToKey4:str = obj["DupToKey4"]
      """  See DupToRelatedToFile  """  
      self.DupToKey5:str = obj["DupToKey5"]
      """  See DupToRelatedToFile  """  
      self.DupToAttachNum:int = obj["DupToAttachNum"]
      """  See DupToRelatedToFile  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetDocumentTypes_input:
   """ Required : 
   tableName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      pass

class GetDocumentTypes_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileAttachmentTableset] = obj["returnObj"]
      pass

class GetVersion_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

