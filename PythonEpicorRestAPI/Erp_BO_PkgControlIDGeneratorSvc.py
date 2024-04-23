import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlIDGeneratorSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlIDGenerators(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlIDGenerators items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlIDGenerators
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlIDGeneratorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlIDGenerators(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlIDGenerators
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlIDGenerators_PkgControlIDCode(PkgControlIDCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlIDGenerator item
   Description: Calls GetByID to retrieve the PkgControlIDGenerator item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlIDGenerator
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators(" + PkgControlIDCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlIDGenerators_PkgControlIDCode(PkgControlIDCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlIDGenerator for the service
   Description: Calls UpdateExt to update PkgControlIDGenerator. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlIDGenerator
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators(" + PkgControlIDCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlIDGenerators_PkgControlIDCode(PkgControlIDCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlIDGenerator item
   Description: Call UpdateExt to delete PkgControlIDGenerator item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlIDGenerator
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators(" + PkgControlIDCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlIDGeneratorListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePkgControlIDGenerator, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePkgControlIDGenerator=" + whereClausePkgControlIDGenerator
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(pkgControlIDCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pkgControlIDCode=" + pkgControlIDCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlIDGenerator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlIDGenerator
   Description: Create the package control ID generator dataset.
   OperationID: GetNewPkgControlIDGenerator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlIDGenerator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlIDGenerator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateButton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateButton
   Description: Generate static or dynamic PCID.
   OperationID: GenerateButton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateButton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateButton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePkgControlIDCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePkgControlIDCode
   Description: Validates the package control ID code.
   OperationID: ChangePkgControlIDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePkgControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePkgControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePkgControlIDType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePkgControlIDType
   Description: Validates the package control ID Type.
   OperationID: ChangePkgControlIDType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePkgControlIDType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePkgControlIDType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePkgCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePkgCode
   Description: Validates the package code.
   OperationID: ChangePkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Validates the part number when changed.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Returns the code / description list of the column.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeWarehouseCode
   Description: Reset the warehouse to printer to blank if the warehouse is set to blank.
   OperationID: ChangeWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportStyles(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportStyles
   Description: Gets the report style values for Package Control ID Generator
   OperationID: GetReportStyles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportStyles_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlIDGeneratorListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlIDGeneratorRow] = obj["value"]
      pass

class Erp_Tablesets_PkgControlIDGeneratorListRow:
   def __init__(self, obj):
      self.NumberToGenerate:int = obj["NumberToGenerate"]
      self.PartDescription:str = obj["PartDescription"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      self.WarehseDesc:str = obj["WarehseDesc"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.PrintName:str = obj["PrintName"]
      self.Description:str = obj["Description"]
      self.NumberOfLabelsToPrint:int = obj["NumberOfLabelsToPrint"]
      self.PrinterID:str = obj["PrinterID"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.CheckAllowMixedLots:bool = obj["CheckAllowMixedLots"]
      self.CheckAllowMixedParts:bool = obj["CheckAllowMixedParts"]
      self.CheckAllowMixedUOMs:bool = obj["CheckAllowMixedUOMs"]
      self.CheckAllowMultipleSerialNumsPerPCID:bool = obj["CheckAllowMultipleSerialNumsPerPCID"]
      self.GenerateStagePCIDs:bool = obj["GenerateStagePCIDs"]
      self.PartNum:str = obj["PartNum"]
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type valid values are Static, Dynamic.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      self.PCIDSGenerated:str = obj["PCIDSGenerated"]
      self.DisableScreen:bool = obj["DisableScreen"]
      self.Plant:str = obj["Plant"]
      self.SuppressPrintLabels:bool = obj["SuppressPrintLabels"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlIDGeneratorRow:
   def __init__(self, obj):
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """   This field will be like the field on the PCID Generate screen that is called from the Material Queue STK-SHP transaction.  The search button will allow searching & Selecting an Active Package Control ID Configuration having Label Print Controlled = False.
When a value is entered or selected, if the Package Code field is empty then the Package Code field should get populated with the Package Code on the selected control ID configuration  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package code  """  
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  Package code description  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.WarehseDesc:str = obj["WarehseDesc"]
      self.NumberToGenerate:int = obj["NumberToGenerate"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.PrintName:str = obj["PrintName"]
      """  Printer name  """  
      self.Description:str = obj["Description"]
      self.NumberOfLabelsToPrint:int = obj["NumberOfLabelsToPrint"]
      self.PrinterID:str = obj["PrinterID"]
      self.GenerateStagePCIDs:bool = obj["GenerateStagePCIDs"]
      self.CheckAllowMixedParts:bool = obj["CheckAllowMixedParts"]
      self.CheckAllowMixedUOMs:bool = obj["CheckAllowMixedUOMs"]
      self.CheckAllowMixedLots:bool = obj["CheckAllowMixedLots"]
      self.CheckAllowMultipleSerialNumsPerPCID:bool = obj["CheckAllowMultipleSerialNumsPerPCID"]
      self.PrintLabels:bool = obj["PrintLabels"]
      self.PkgControlType:str = obj["PkgControlType"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   pulated with all the Warehouses owned or shared with the current site.  The Search will allow searching & selecting any Warehouse owned or shared with the current site.  Users can also enter a Warehouse ID
When a Warehouse is Entered/Selected, the Printer field should be populated with the Default Printer for the Warehouse  """  
      self.HHForm:bool = obj["HHForm"]
      self.PCIDSGenerated:str = obj["PCIDSGenerated"]
      self.DisableScreen:bool = obj["DisableScreen"]
      self.Plant:str = obj["Plant"]
      self.DisableWarehouse:bool = obj["DisableWarehouse"]
      """  Disable Warehouse in the PCID Generator screen if true as sometimes we require to pass in and force the warehouse to not be modified,  """  
      self.SuppressPrintLabels:bool = obj["SuppressPrintLabels"]
      self.DisableNumberToGenerate:bool = obj["DisableNumberToGenerate"]
      self.StyleNum:int = obj["StyleNum"]
      self.StyleDescription:str = obj["StyleDescription"]
      self.DisableNumLblsRptStyle:bool = obj["DisableNumLblsRptStyle"]
      self.PkgControlOutboundContainer:bool = obj["PkgControlOutboundContainer"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangePartNum_input:
   """ Required : 
   ds
   ipPartNum
   warehouseFrozen
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      self.ipPartNum:str = obj["ipPartNum"]
      """  The part number.  """  
      self.warehouseFrozen:bool = obj["warehouseFrozen"]
      """  don't change warehouse if a warehouse is passed in from another UI  """  
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePkgCode_input:
   """ Required : 
   ds
   ipPkgCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      self.ipPkgCode:str = obj["ipPkgCode"]
      """  Package code.  """  
      pass

class ChangePkgCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePkgControlIDCode_input:
   """ Required : 
   ds
   ipPkgControlIDCode
   warehouseFrozen
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      self.ipPkgControlIDCode:str = obj["ipPkgControlIDCode"]
      """  The package control ID code.  """  
      self.warehouseFrozen:bool = obj["warehouseFrozen"]
      """  to enable change of warehouse  """  
      pass

class ChangePkgControlIDCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePkgControlIDType_input:
   """ Required : 
   ds
   pkgControlIDType
   warehouseFrozen
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      self.pkgControlIDType:str = obj["pkgControlIDType"]
      """  package control ID Type.  """  
      self.warehouseFrozen:bool = obj["warehouseFrozen"]
      """  to not change warehouse on the bo side  """  
      pass

class ChangePkgControlIDType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeWarehouseCode_input:
   """ Required : 
   ipWarehouseCode
   ds
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code.  """  
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

class ChangeWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PkgControlIDGeneratorListRow:
   def __init__(self, obj):
      self.NumberToGenerate:int = obj["NumberToGenerate"]
      self.PartDescription:str = obj["PartDescription"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      self.WarehseDesc:str = obj["WarehseDesc"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.PrintName:str = obj["PrintName"]
      self.Description:str = obj["Description"]
      self.NumberOfLabelsToPrint:int = obj["NumberOfLabelsToPrint"]
      self.PrinterID:str = obj["PrinterID"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.CheckAllowMixedLots:bool = obj["CheckAllowMixedLots"]
      self.CheckAllowMixedParts:bool = obj["CheckAllowMixedParts"]
      self.CheckAllowMixedUOMs:bool = obj["CheckAllowMixedUOMs"]
      self.CheckAllowMultipleSerialNumsPerPCID:bool = obj["CheckAllowMultipleSerialNumsPerPCID"]
      self.GenerateStagePCIDs:bool = obj["GenerateStagePCIDs"]
      self.PartNum:str = obj["PartNum"]
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type valid values are Static, Dynamic.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      self.PCIDSGenerated:str = obj["PCIDSGenerated"]
      self.DisableScreen:bool = obj["DisableScreen"]
      self.Plant:str = obj["Plant"]
      self.SuppressPrintLabels:bool = obj["SuppressPrintLabels"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlIDGeneratorListTableset:
   def __init__(self, obj):
      self.PkgControlIDGeneratorList:list[Erp_Tablesets_PkgControlIDGeneratorListRow] = obj["PkgControlIDGeneratorList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlIDGeneratorRow:
   def __init__(self, obj):
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """   This field will be like the field on the PCID Generate screen that is called from the Material Queue STK-SHP transaction.  The search button will allow searching & Selecting an Active Package Control ID Configuration having Label Print Controlled = False.
When a value is entered or selected, if the Package Code field is empty then the Package Code field should get populated with the Package Code on the selected control ID configuration  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package code  """  
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  Package code description  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.WarehseDesc:str = obj["WarehseDesc"]
      self.NumberToGenerate:int = obj["NumberToGenerate"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.PrintName:str = obj["PrintName"]
      """  Printer name  """  
      self.Description:str = obj["Description"]
      self.NumberOfLabelsToPrint:int = obj["NumberOfLabelsToPrint"]
      self.PrinterID:str = obj["PrinterID"]
      self.GenerateStagePCIDs:bool = obj["GenerateStagePCIDs"]
      self.CheckAllowMixedParts:bool = obj["CheckAllowMixedParts"]
      self.CheckAllowMixedUOMs:bool = obj["CheckAllowMixedUOMs"]
      self.CheckAllowMixedLots:bool = obj["CheckAllowMixedLots"]
      self.CheckAllowMultipleSerialNumsPerPCID:bool = obj["CheckAllowMultipleSerialNumsPerPCID"]
      self.PrintLabels:bool = obj["PrintLabels"]
      self.PkgControlType:str = obj["PkgControlType"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   pulated with all the Warehouses owned or shared with the current site.  The Search will allow searching & selecting any Warehouse owned or shared with the current site.  Users can also enter a Warehouse ID
When a Warehouse is Entered/Selected, the Printer field should be populated with the Default Printer for the Warehouse  """  
      self.HHForm:bool = obj["HHForm"]
      self.PCIDSGenerated:str = obj["PCIDSGenerated"]
      self.DisableScreen:bool = obj["DisableScreen"]
      self.Plant:str = obj["Plant"]
      self.DisableWarehouse:bool = obj["DisableWarehouse"]
      """  Disable Warehouse in the PCID Generator screen if true as sometimes we require to pass in and force the warehouse to not be modified,  """  
      self.SuppressPrintLabels:bool = obj["SuppressPrintLabels"]
      self.DisableNumberToGenerate:bool = obj["DisableNumberToGenerate"]
      self.StyleNum:int = obj["StyleNum"]
      self.StyleDescription:str = obj["StyleDescription"]
      self.DisableNumLblsRptStyle:bool = obj["DisableNumLblsRptStyle"]
      self.PkgControlOutboundContainer:bool = obj["PkgControlOutboundContainer"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlIDGeneratorTableset:
   def __init__(self, obj):
      self.PkgControlIDGenerator:list[Erp_Tablesets_PkgControlIDGeneratorRow] = obj["PkgControlIDGenerator"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPkgControlIDGeneratorTableset:
   def __init__(self, obj):
      self.PkgControlIDGenerator:list[Erp_Tablesets_PkgControlIDGeneratorRow] = obj["PkgControlIDGenerator"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateButton_input:
   """ Required : 
   ds
   ds2
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      self.ds2      #schema had no properties on an object.
      """  Package control ID generator row.  """  
      pass

class GenerateButton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      self.pcidsGeneratedMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   pkgControlIDCode
   """  
   def __init__(self, obj):
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name.  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDGeneratorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPkgControlIDGenerator_input:
   """ Required : 
   isHHForm
   ipPkgControlType
   """  
   def __init__(self, obj):
      self.isHHForm:bool = obj["isHHForm"]
      """  Set to true if invoked from the hand held.  """  
      self.ipPkgControlType:str = obj["ipPkgControlType"]
      """  The package control type.  """  
      pass

class GetNewPkgControlIDGenerator_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["returnObj"]
      pass

class GetReportStyles_input:
   """ Required : 
   pkgControlType
   pkgControlIDCode
   pkgCode
   """  
   def __init__(self, obj):
      self.pkgControlType:str = obj["pkgControlType"]
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      self.pkgCode:str = obj["pkgCode"]
      pass

class GetReportStyles_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePkgControlIDGenerator
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePkgControlIDGenerator:str = obj["whereClausePkgControlIDGenerator"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlIDGeneratorTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlIDGeneratorTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["ds"]
      pass

      """  output parameters  """  

