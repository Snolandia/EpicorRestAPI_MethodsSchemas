import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FSWarrCdSvc
# Description: Field Service Warranty Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FSWarrCds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSWarrCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSWarrCds
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSWarrCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/FSWarrCds",headers=creds) as resp:
           return await resp.json()

async def post_FSWarrCds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSWarrCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSWarrCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSWarrCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/FSWarrCds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSWarrCds_Company_WarrantyCode(Company, WarrantyCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSWarrCd item
   Description: Calls GetByID to retrieve the FSWarrCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSWarrCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarrantyCode: Desc: WarrantyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSWarrCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/FSWarrCds(" + Company + "," + WarrantyCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSWarrCds_Company_WarrantyCode(Company, WarrantyCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSWarrCd for the service
   Description: Calls UpdateExt to update FSWarrCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSWarrCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarrantyCode: Desc: WarrantyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSWarrCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/FSWarrCds(" + Company + "," + WarrantyCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSWarrCds_Company_WarrantyCode(Company, WarrantyCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSWarrCd item
   Description: Call UpdateExt to delete FSWarrCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSWarrCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarrantyCode: Desc: WarrantyCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/FSWarrCds(" + Company + "," + WarrantyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSWarrCds_Company_WarrantyCode_LangDescs(Company, WarrantyCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LangDescs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LangDescs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarrantyCode: Desc: WarrantyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/FSWarrCds(" + Company + "," + WarrantyCode + ")/LangDescs",headers=creds) as resp:
           return await resp.json()

async def get_FSWarrCds_Company_WarrantyCode_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, WarrantyCode, TableName, Key1, Key2, Key3, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarrantyCode: Desc: WarrantyCode   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/FSWarrCds(" + Company + "," + WarrantyCode + ")/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LangDescs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LangDescs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LangDescs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/LangDescs",headers=creds) as resp:
           return await resp.json()

async def post_LangDescs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LangDescs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LangDescRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/LangDescs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LangDesc for the service
   Description: Calls UpdateExt to update LangDesc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LangDesc item
   Description: Call UpdateExt to delete LangDesc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSWarrCdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFSWarrCd, whereClauseLangDesc, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseFSWarrCd=" + whereClauseFSWarrCd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLangDesc=" + whereClauseLangDesc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(warrantyCode, epicorHeaders = None):
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
   params += "warrantyCode=" + warrantyCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSWarrCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSWarrCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSWarrCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSWarrCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSWarrCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLangDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLangDesc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLangDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLangDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLangDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSWarrCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSWarrCdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSWarrCdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSWarrCdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSWarrCdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LangDescRow] = obj["value"]
      pass

class Erp_Tablesets_FSWarrCdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique identifer of the warranty assigned by the user.  """  
      self.WarrDescription:str = obj["WarrDescription"]
      """  Description of the warranty.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The number of days, months, or years the material is covered by the warranty if FSWarrCD.MatCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The number of days, months, or years the Labor is covered by the warranty if FSWarrCd.LabCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The number of days, months, or years the Misc Charges are covered by the warranty if FSWarrCd.MiscCovered = True. FSWarrCd.MiscMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Determines whether the FSWarrCd.MaterialDuration value is in days, months or years.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Determines whether the FSWarrCd.LaborDuration value is in days, months or years.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Determines whether the FSWarrCd.MiscDuration value is in days, months or years.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments about the Warranty. These will print on the Sales Order Acknowledgement Form when a part that is associated with this Warranty appears on the order.  """  
      self.OnSite:bool = obj["OnSite"]
      """  Determines whether or not the Warranty covers onsite visits.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Determines whether or not material costs are covered by the warranty.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Determines whether labor costs are covered by the warranty.  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Determines whether or not Miscellaneous costs are covered by the warranty.  """  
      self.GlobalFSWarrCd:bool = obj["GlobalFSWarrCd"]
      """  Marks this FSWarrCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSWarrCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique identifer of the warranty assigned by the user.  """  
      self.WarrDescription:str = obj["WarrDescription"]
      """  Description of the warranty.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The number of days, months, or years the material is covered by the warranty if FSWarrCD.MatCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The number of days, months, or years the Labor is covered by the warranty if FSWarrCd.LabCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The number of days, months, or years the Misc Charges are covered by the warranty if FSWarrCd.MiscCovered = True. FSWarrCd.MiscMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Determines whether the FSWarrCd.MaterialDuration value is in days, months or years.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Determines whether the FSWarrCd.LaborDuration value is in days, months or years.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Determines whether the FSWarrCd.MiscDuration value is in days, months or years.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments about the Warranty. These will print on the Sales Order Acknowledgement Form when a part that is associated with this Warranty appears on the order.  """  
      self.OnSite:bool = obj["OnSite"]
      """  Determines whether or not the Warranty covers onsite visits.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Determines whether or not material costs are covered by the warranty.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Determines whether labor costs are covered by the warranty.  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Determines whether or not Miscellaneous costs are covered by the warranty.  """  
      self.GlobalFSWarrCd:bool = obj["GlobalFSWarrCd"]
      """  Marks this FSWarrCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warranty has to be synchronized with Epicor FSA application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Name of table that this data is related  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Key1:str = obj["Key1"]
      """  Contains values that represent the key1 to the foreign record that this record is related.  """  
      self.Key2:str = obj["Key2"]
      """  key2  of  the foreign record  """  
      self.Key3:str = obj["Key3"]
      """  key3 of the foreign record  """  
      self.Description:str = obj["Description"]
      """  Language Description  """  
      self.GlobalLangDesc:bool = obj["GlobalLangDesc"]
      """  Marks this LangDesc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   warrantyCode
   """  
   def __init__(self, obj):
      self.warrantyCode:str = obj["warrantyCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FSWarrCdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique identifer of the warranty assigned by the user.  """  
      self.WarrDescription:str = obj["WarrDescription"]
      """  Description of the warranty.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The number of days, months, or years the material is covered by the warranty if FSWarrCD.MatCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The number of days, months, or years the Labor is covered by the warranty if FSWarrCd.LabCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The number of days, months, or years the Misc Charges are covered by the warranty if FSWarrCd.MiscCovered = True. FSWarrCd.MiscMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Determines whether the FSWarrCd.MaterialDuration value is in days, months or years.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Determines whether the FSWarrCd.LaborDuration value is in days, months or years.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Determines whether the FSWarrCd.MiscDuration value is in days, months or years.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments about the Warranty. These will print on the Sales Order Acknowledgement Form when a part that is associated with this Warranty appears on the order.  """  
      self.OnSite:bool = obj["OnSite"]
      """  Determines whether or not the Warranty covers onsite visits.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Determines whether or not material costs are covered by the warranty.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Determines whether labor costs are covered by the warranty.  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Determines whether or not Miscellaneous costs are covered by the warranty.  """  
      self.GlobalFSWarrCd:bool = obj["GlobalFSWarrCd"]
      """  Marks this FSWarrCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSWarrCdListTableset:
   def __init__(self, obj):
      self.FSWarrCdList:list[Erp_Tablesets_FSWarrCdListRow] = obj["FSWarrCdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSWarrCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique identifer of the warranty assigned by the user.  """  
      self.WarrDescription:str = obj["WarrDescription"]
      """  Description of the warranty.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The number of days, months, or years the material is covered by the warranty if FSWarrCD.MatCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The number of days, months, or years the Labor is covered by the warranty if FSWarrCd.LabCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The number of days, months, or years the Misc Charges are covered by the warranty if FSWarrCd.MiscCovered = True. FSWarrCd.MiscMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Determines whether the FSWarrCd.MaterialDuration value is in days, months or years.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Determines whether the FSWarrCd.LaborDuration value is in days, months or years.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Determines whether the FSWarrCd.MiscDuration value is in days, months or years.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments about the Warranty. These will print on the Sales Order Acknowledgement Form when a part that is associated with this Warranty appears on the order.  """  
      self.OnSite:bool = obj["OnSite"]
      """  Determines whether or not the Warranty covers onsite visits.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Determines whether or not material costs are covered by the warranty.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Determines whether labor costs are covered by the warranty.  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Determines whether or not Miscellaneous costs are covered by the warranty.  """  
      self.GlobalFSWarrCd:bool = obj["GlobalFSWarrCd"]
      """  Marks this FSWarrCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warranty has to be synchronized with Epicor FSA application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSWarrCdTableset:
   def __init__(self, obj):
      self.FSWarrCd:list[Erp_Tablesets_FSWarrCdRow] = obj["FSWarrCd"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Name of table that this data is related  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Key1:str = obj["Key1"]
      """  Contains values that represent the key1 to the foreign record that this record is related.  """  
      self.Key2:str = obj["Key2"]
      """  key2  of  the foreign record  """  
      self.Key3:str = obj["Key3"]
      """  key3 of the foreign record  """  
      self.Description:str = obj["Description"]
      """  Language Description  """  
      self.GlobalLangDesc:bool = obj["GlobalLangDesc"]
      """  Marks this LangDesc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtFSWarrCdTableset:
   def __init__(self, obj):
      self.FSWarrCd:list[Erp_Tablesets_FSWarrCdRow] = obj["FSWarrCd"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   warrantyCode
   """  
   def __init__(self, obj):
      self.warrantyCode:str = obj["warrantyCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSWarrCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FSWarrCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FSWarrCdTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
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
      self.returnObj:list[Erp_Tablesets_FSWarrCdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFSWarrCd_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FSWarrCdTableset] = obj["ds"]
      pass

class GetNewFSWarrCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FSWarrCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLangDesc_input:
   """ Required : 
   ds
   tableName
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FSWarrCdTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewLangDesc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FSWarrCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFSWarrCd
   whereClauseLangDesc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSWarrCd:str = obj["whereClauseFSWarrCd"]
      self.whereClauseLangDesc:str = obj["whereClauseLangDesc"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSWarrCdTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtFSWarrCdTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFSWarrCdTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FSWarrCdTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FSWarrCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

