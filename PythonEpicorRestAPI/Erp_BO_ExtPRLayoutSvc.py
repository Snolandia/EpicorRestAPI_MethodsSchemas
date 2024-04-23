import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ExtPRLayoutSvc
# Description: ExtPRLayoutSvc class
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRLayouts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPRLayouts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRLayouts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportLayoutRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts",headers=creds) as resp:
           return await resp.json()

async def post_ExtPRLayouts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPRLayouts_Company_PayExportLayoutID(Company, PayExportLayoutID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRLayout item
   Description: Calls GetByID to retrieve the ExtPRLayout item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRLayout
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPRLayouts_Company_PayExportLayoutID(Company, PayExportLayoutID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPRLayout for the service
   Description: Calls UpdateExt to update ExtPRLayout. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRLayout
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPRLayouts_Company_PayExportLayoutID(Company, PayExportLayoutID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPRLayout item
   Description: Call UpdateExt to delete ExtPRLayout item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRLayout
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRLayouts_Company_PayExportLayoutID_ExtPRExportSeqs(Company, PayExportLayoutID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtPRExportSeqs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPRExportSeqs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")/ExtPRExportSeqs",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRLayouts_Company_PayExportLayoutID_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company, PayExportLayoutID, SchemaName, TableName, ColumnName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRExportSeq item
   Description: Calls GetByID to retrieve the ExtPRExportSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRExportSeq1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRExportSeqs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPRExportSeqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRExportSeqs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs",headers=creds) as resp:
           return await resp.json()

async def post_ExtPRExportSeqs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRExportSeqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company, PayExportLayoutID, SchemaName, TableName, ColumnName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRExportSeq item
   Description: Calls GetByID to retrieve the ExtPRExportSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRExportSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company, PayExportLayoutID, SchemaName, TableName, ColumnName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPRExportSeq for the service
   Description: Calls UpdateExt to update ExtPRExportSeq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRExportSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company, PayExportLayoutID, SchemaName, TableName, ColumnName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPRExportSeq item
   Description: Call UpdateExt to delete ExtPRExportSeq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRExportSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayExportLayoutID: Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportLayoutListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtPRExportLayout, whereClauseExtPRExportSeq, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseExtPRExportLayout=" + whereClauseExtPRExportLayout
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtPRExportSeq=" + whereClauseExtPRExportSeq
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(payExportLayoutID, epicorHeaders = None):
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
   params += "payExportLayoutID=" + payExportLayoutID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_MoveOnePosition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveOnePosition
   Description: This method moves the layout field sequences Up/Down one position in the  grid and returns the whole updated data table.
   OperationID: MoveOnePosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getSourceTables(epicorHeaders = None):
   """  
   Summary: Invoke method getSourceTables
   Description: This method is used to fill the source table combo since this table doesn't have its own BO.
   OperationID: getSourceTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/getSourceTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_getSourceFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getSourceFields
   Description: This method is used to fill the source field combo since this table doesn't have its own BO.
   OperationID: getSourceFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getSourceFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getSourceFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_changeColumnName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method changeColumnName
   Description: Call this method to get the column description (Link Field)
   OperationID: changeColumnName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/changeColumnName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/changeColumnName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_changeLayoutDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method changeLayoutDescription
   Description: Call this method to validate if the description already exists.
   OperationID: changeLayoutDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/changeLayoutDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/changeLayoutDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LayoutIDExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LayoutIDExists
   Description: This method is called to check if a  Layout id exists
   OperationID: LayoutIDExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LayoutIDExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LayoutIDExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPredefinedLayout(epicorHeaders = None):
   """  
   Summary: Invoke method GetPredefinedLayout
   Description: Creates and returns the External Layout Tableset using the default ADP layout.
   OperationID: GetPredefinedLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPredefinedLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UpdateExportLayoutFieldParent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExportLayoutFieldParent
   Description: Update Parent ID for ExtPRExportSeq during parent creation for new ADP layouts.
   OperationID: UpdateExportLayoutFieldParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExportLayoutFieldParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExportLayoutFieldParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPRExportLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPRExportLayout
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRExportLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRExportLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRExportLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPRExportSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPRExportSeq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRExportSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRExportSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRExportSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRExportLayoutListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRExportLayoutRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportSeqRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRExportSeqRow] = obj["value"]
      pass

class Erp_Tablesets_ExtPRExportLayoutListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Payroll layout ID  """  
      self.Description:str = obj["Description"]
      """  Payroll layout description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRExportLayoutRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Payroll layout ID  """  
      self.Description:str = obj["Description"]
      """  Payroll layout description  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  Short Character #1  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  Short Character #2  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  Short Character #3  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  Short Character #4  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  Short Character #5  """  
      self.Character01:str = obj["Character01"]
      """  Long Character #1  """  
      self.Character02:str = obj["Character02"]
      """  Long Character #2  """  
      self.Character03:str = obj["Character03"]
      """  Long Character #3  """  
      self.Character04:str = obj["Character04"]
      """  Long Character #4  """  
      self.Character05:str = obj["Character05"]
      """  Long Character #5  """  
      self.Number01:int = obj["Number01"]
      """  Numeric #1  """  
      self.Number02:int = obj["Number02"]
      """  Numeric #2  """  
      self.Number03:int = obj["Number03"]
      """  Numeric #3  """  
      self.Number04:int = obj["Number04"]
      """  Numeric #4  """  
      self.Number05:int = obj["Number05"]
      """  Numeric #5  """  
      self.Number06:int = obj["Number06"]
      """  Integer #1  """  
      self.Number07:int = obj["Number07"]
      """  Integer #2  """  
      self.Number08:int = obj["Number08"]
      """  Integer #3  """  
      self.Number09:int = obj["Number09"]
      """  Integer #4  """  
      self.Number10:int = obj["Number10"]
      """  Integer #5  """  
      self.Date01:str = obj["Date01"]
      """  Date #1  """  
      self.Date02:str = obj["Date02"]
      """  Date #2  """  
      self.Date03:str = obj["Date03"]
      """  Date #3  """  
      self.Checkbox01:bool = obj["Checkbox01"]
      """  Boolean #1  """  
      self.Checkbox02:bool = obj["Checkbox02"]
      """  Boolean #2  """  
      self.Checkbox03:bool = obj["Checkbox03"]
      """  Boolean #3  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRExportSeqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Payroll Layout ID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Epicor Source Schema  """  
      self.TableName:str = obj["TableName"]
      """  Epicor Source Table  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Epicor Source Column  """  
      self.Seq:int = obj["Seq"]
      """  Order of the fields to be exported  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ColumnTitle:str = obj["ColumnTitle"]
      """  ColumnTitle  """  
      self.Description:str = obj["Description"]
      """  Column Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   payExportLayoutID
   """  
   def __init__(self, obj):
      self.payExportLayoutID:str = obj["payExportLayoutID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ExtPRExportLayoutListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Payroll layout ID  """  
      self.Description:str = obj["Description"]
      """  Payroll layout description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRExportLayoutListTableset:
   def __init__(self, obj):
      self.ExtPRExportLayoutList:list[Erp_Tablesets_ExtPRExportLayoutListRow] = obj["ExtPRExportLayoutList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtPRExportLayoutRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Payroll layout ID  """  
      self.Description:str = obj["Description"]
      """  Payroll layout description  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  Short Character #1  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  Short Character #2  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  Short Character #3  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  Short Character #4  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  Short Character #5  """  
      self.Character01:str = obj["Character01"]
      """  Long Character #1  """  
      self.Character02:str = obj["Character02"]
      """  Long Character #2  """  
      self.Character03:str = obj["Character03"]
      """  Long Character #3  """  
      self.Character04:str = obj["Character04"]
      """  Long Character #4  """  
      self.Character05:str = obj["Character05"]
      """  Long Character #5  """  
      self.Number01:int = obj["Number01"]
      """  Numeric #1  """  
      self.Number02:int = obj["Number02"]
      """  Numeric #2  """  
      self.Number03:int = obj["Number03"]
      """  Numeric #3  """  
      self.Number04:int = obj["Number04"]
      """  Numeric #4  """  
      self.Number05:int = obj["Number05"]
      """  Numeric #5  """  
      self.Number06:int = obj["Number06"]
      """  Integer #1  """  
      self.Number07:int = obj["Number07"]
      """  Integer #2  """  
      self.Number08:int = obj["Number08"]
      """  Integer #3  """  
      self.Number09:int = obj["Number09"]
      """  Integer #4  """  
      self.Number10:int = obj["Number10"]
      """  Integer #5  """  
      self.Date01:str = obj["Date01"]
      """  Date #1  """  
      self.Date02:str = obj["Date02"]
      """  Date #2  """  
      self.Date03:str = obj["Date03"]
      """  Date #3  """  
      self.Checkbox01:bool = obj["Checkbox01"]
      """  Boolean #1  """  
      self.Checkbox02:bool = obj["Checkbox02"]
      """  Boolean #2  """  
      self.Checkbox03:bool = obj["Checkbox03"]
      """  Boolean #3  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRExportSeqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Payroll Layout ID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Epicor Source Schema  """  
      self.TableName:str = obj["TableName"]
      """  Epicor Source Table  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Epicor Source Column  """  
      self.Seq:int = obj["Seq"]
      """  Order of the fields to be exported  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ColumnTitle:str = obj["ColumnTitle"]
      """  ColumnTitle  """  
      self.Description:str = obj["Description"]
      """  Column Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRExportSrcFldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRExportSrcFldTableset:
   def __init__(self, obj):
      self.ExtPRExportSrcFld:list[Erp_Tablesets_ExtPRExportSrcFldRow] = obj["ExtPRExportSrcFld"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtPRExportSrcTblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRExportSrcTblTableset:
   def __init__(self, obj):
      self.ExtPRExportSrcTbl:list[Erp_Tablesets_ExtPRExportSrcTblRow] = obj["ExtPRExportSrcTbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtPRLayoutTableset:
   def __init__(self, obj):
      self.ExtPRExportLayout:list[Erp_Tablesets_ExtPRExportLayoutRow] = obj["ExtPRExportLayout"]
      self.ExtPRExportSeq:list[Erp_Tablesets_ExtPRExportSeqRow] = obj["ExtPRExportSeq"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtExtPRLayoutTableset:
   def __init__(self, obj):
      self.ExtPRExportLayout:list[Erp_Tablesets_ExtPRExportLayoutRow] = obj["ExtPRExportLayout"]
      self.ExtPRExportSeq:list[Erp_Tablesets_ExtPRExportSeqRow] = obj["ExtPRExportSeq"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   payExportLayoutID
   """  
   def __init__(self, obj):
      self.payExportLayoutID:str = obj["payExportLayoutID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtPRExportLayoutListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewExtPRExportLayout_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

class GetNewExtPRExportLayout_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtPRExportSeq_input:
   """ Required : 
   ds
   payExportLayoutID
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      self.payExportLayoutID:str = obj["payExportLayoutID"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class GetNewExtPRExportSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPredefinedLayout_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseExtPRExportLayout
   whereClauseExtPRExportSeq
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtPRExportLayout:str = obj["whereClauseExtPRExportLayout"]
      self.whereClauseExtPRExportSeq:str = obj["whereClauseExtPRExportSeq"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["returnObj"]
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

class LayoutIDExists_input:
   """ Required : 
   layoutID
   """  
   def __init__(self, obj):
      self.layoutID:str = obj["layoutID"]
      pass

class LayoutIDExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class MoveOnePosition_input:
   """ Required : 
   layoutID
   schemaName
   tableName
   columnName
   displayOrder
   moveDir
   """  
   def __init__(self, obj):
      self.layoutID:str = obj["layoutID"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      self.displayOrder:int = obj["displayOrder"]
      self.moveDir:str = obj["moveDir"]
      pass

class MoveOnePosition_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["returnObj"]
      pass

class UpdateExportLayoutFieldParent_input:
   """ Required : 
   payExportLayoutID
   ds
   """  
   def __init__(self, obj):
      self.payExportLayoutID:str = obj["payExportLayoutID"]
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

class UpdateExportLayoutFieldParent_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtPRLayoutTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtPRLayoutTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class changeColumnName_input:
   """ Required : 
   proposedColumnName
   ds
   """  
   def __init__(self, obj):
      self.proposedColumnName:str = obj["proposedColumnName"]
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

class changeColumnName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class changeLayoutDescription_input:
   """ Required : 
   proposedDescription
   ds
   """  
   def __init__(self, obj):
      self.proposedDescription:str = obj["proposedDescription"]
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

class changeLayoutDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class getSourceFields_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class getSourceFields_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRExportSrcFldTableset] = obj["returnObj"]
      pass

class getSourceTables_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRExportSrcTblTableset] = obj["returnObj"]
      pass

