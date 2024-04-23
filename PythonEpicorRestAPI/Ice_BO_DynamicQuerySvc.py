import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.DynamicQuerySvc
# Description: This is the DynamicQuery object. It has various methods for executing a query.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynamicQueries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynamicQueries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DynamicQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID(Company, QueryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynamicQuery item
   Description: Calls GetByID to retrieve the DynamicQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynamicQuery
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DynamicQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryCtrls(Company, QueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCtrls",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryCtrls_Company_QueryID_ControlID(Company, QueryID, ControlID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrl item
   Description: Calls GetByID to retrieve the QueryCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryCustomActions(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryCustomActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCustomActions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCustomActions",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryCustomActions_Company_QueryID_ActionID(Company, QueryID, ActionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCustomAction item
   Description: Calls GetByID to retrieve the QueryCustomAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomAction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCustomActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCustomActions(" + Company + "," + QueryID + "," + ActionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryExecuteSettings(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryExecuteSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryExecuteSettings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryExecuteSettings",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryExecuteSettings_Company_QueryID_SettingID(Company, QueryID, SettingID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryExecuteSetting item
   Description: Calls GetByID to retrieve the QueryExecuteSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSetting1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SettingID: Desc: SettingID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryExecuteSettings(" + Company + "," + QueryID + "," + SettingID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryParameters(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryParameters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameters1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryParameters",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryParameters_Company_QueryID_ParameterID(Company, QueryID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameter item
   Description: Calls GetByID to retrieve the QueryParameter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameter1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryParameters(" + Company + "," + QueryID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryReferences(Company, QueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryReferences items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryReferences1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryReferences",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryReferences_Company_QueryID_ReferenceID(Company, QueryID, ReferenceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryReference item
   Description: Calls GetByID to retrieve the QueryReference item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReference1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryReferenceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QuerySubQueries(Company, QueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuerySubQueries items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySubQueries1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QuerySubQueries",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QuerySubQueries_Company_QueryID_SubQueryID(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySubQuery item
   Description: Calls GetByID to retrieve the QuerySubQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQuery1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySubQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryUpdateFields(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateFields1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateFields",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryUpdateFields_Company_QueryID_MapTableName_MapFieldName_Direction(Company, QueryID, MapTableName, MapFieldName, Direction, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateField item
   Description: Calls GetByID to retrieve the QueryUpdateField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateField1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param MapTableName: Desc: MapTableName   Required: True   Allow empty value : True
      :param MapFieldName: Desc: MapFieldName   Required: True   Allow empty value : True
      :param Direction: Desc: Direction   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateFields(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryUpdateSettings(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateSettings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateSettings",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryUpdateSettings_Company_QueryID(Company, QueryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateSetting item
   Description: Calls GetByID to retrieve the QueryUpdateSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSetting1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateSettings(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryValueSetItems(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryValueSetItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryValueSetItems1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryValueSetItems",headers=creds) as resp:
           return await resp.json()

async def get_DynamicQueries_Company_QueryID_QueryValueSetItems_Company_QueryID_ValueSetID_ItemValue(Company, QueryID, ValueSetID, ItemValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryValueSetItem item
   Description: Calls GetByID to retrieve the QueryValueSetItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItem1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ValueSetID: Desc: ValueSetID   Required: True   Allow empty value : True
      :param ItemValue: Desc: ItemValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrls_Company_QueryID_ControlID(Company, QueryID, ControlID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrl item
   Description: Calls GetByID to retrieve the QueryCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrls_Company_QueryID_ControlID_QueryCtrlValues(Company, QueryID, ControlID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrlValues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrlValues1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValues",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrls_Company_QueryID_ControlID_QueryCtrlValues_Company_QueryID_ControlID_ID(Company, QueryID, ControlID, ID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrlValue item
   Description: Calls GetByID to retrieve the QueryCtrlValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValue1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param ID: Desc: ID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValues(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrlValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrlValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrlValues",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlValues_Company_QueryID_ControlID_ID(Company, QueryID, ControlID, ID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrlValue item
   Description: Calls GetByID to retrieve the QueryCtrlValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param ID: Desc: ID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrlValues(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCustomActions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryCustomActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCustomActions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCustomActions",headers=creds) as resp:
           return await resp.json()

async def get_QueryCustomActions_Company_QueryID_ActionID(Company, QueryID, ActionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCustomAction item
   Description: Calls GetByID to retrieve the QueryCustomAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCustomActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCustomActions(" + Company + "," + QueryID + "," + ActionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryExecuteSettings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryExecuteSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryExecuteSettings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryExecuteSettings",headers=creds) as resp:
           return await resp.json()

async def get_QueryExecuteSettings_Company_QueryID_SettingID(Company, QueryID, SettingID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryExecuteSetting item
   Description: Calls GetByID to retrieve the QueryExecuteSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SettingID: Desc: SettingID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryExecuteSettings(" + Company + "," + QueryID + "," + SettingID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryParameters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryParameters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameters",headers=creds) as resp:
           return await resp.json()

async def get_QueryParameters_Company_QueryID_ParameterID(Company, QueryID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameter item
   Description: Calls GetByID to retrieve the QueryParameter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameters(" + Company + "," + QueryID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryReferences(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryReferences items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryReferences
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences",headers=creds) as resp:
           return await resp.json()

async def get_QueryReferences_Company_QueryID_ReferenceID(Company, QueryID, ReferenceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryReference item
   Description: Calls GetByID to retrieve the QueryReference item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReference
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryReferenceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryReferences_Company_QueryID_ReferenceID_QueryParameterBindings(Company, QueryID, ReferenceID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryParameterBindings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameterBindings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindings",headers=creds) as resp:
           return await resp.json()

async def get_QueryReferences_Company_QueryID_ReferenceID_QueryParameterBindings_Company_QueryID_ReferenceID_ParameterID(Company, QueryID, ReferenceID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameterBinding item
   Description: Calls GetByID to retrieve the QueryParameterBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBinding1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindings(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryParameterBindings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryParameterBindings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameterBindings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameterBindings",headers=creds) as resp:
           return await resp.json()

async def get_QueryParameterBindings_Company_QueryID_ReferenceID_ParameterID(Company, QueryID, ReferenceID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameterBinding item
   Description: Calls GetByID to retrieve the QueryParameterBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBinding
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameterBindings(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuerySubQueries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySubQueries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySubQuery item
   Description: Calls GetByID to retrieve the QuerySubQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQuery
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySubQueryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryRelations(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryRelations items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelations1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelations",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryRelations_Company_QueryID_SubQueryID_RelationID(Company, QueryID, SubQueryID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelation item
   Description: Calls GetByID to retrieve the QueryRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelation1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QuerySortBies(Company, QueryID, SubQueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuerySortBies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySortBies1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortBies",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QuerySortBies_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySortBy item
   Description: Calls GetByID to retrieve the QuerySortBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortBy1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySortByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortBies(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryWhereItems(Company, QueryID, SubQueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryWhereItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryWhereItems1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItems",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryWhereItems_SysRowID(Company, QueryID, SubQueryID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryWhereItem item
   Description: Calls GetByID to retrieve the QueryWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItem1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItems(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryGroupBies(Company, QueryID, SubQueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryGroupBies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryGroupBies1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupBies",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryGroupBies_Company_QueryID_SubQueryID_GroupByID(Company, QueryID, SubQueryID, GroupByID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryGroupBy item
   Description: Calls GetByID to retrieve the QueryGroupBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupBy1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param GroupByID: Desc: GroupByID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryGroupByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupBies(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryTables(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryTables1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTables",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueries_Company_QueryID_SubQueryID_QueryTables_Company_QueryID_SubQueryID_TableID(Company, QueryID, SubQueryID, TableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryTable item
   Description: Calls GetByID to retrieve the QueryTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTable1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryRelations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelations_Company_QueryID_SubQueryID_RelationID(Company, QueryID, SubQueryID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelation item
   Description: Calls GetByID to retrieve the QueryRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelations_Company_QueryID_SubQueryID_RelationID_QueryRelationFields(Company, QueryID, SubQueryID, RelationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryRelationFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelationFields1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFields",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelations_Company_QueryID_SubQueryID_RelationID_QueryRelationFields_Company_QueryID_SubQueryID_RelationID_Seq(Company, QueryID, SubQueryID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelationField item
   Description: Calls GetByID to retrieve the QueryRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationField1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFields(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryRelationFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelationFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelationFields",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationFields_Company_QueryID_SubQueryID_RelationID_Seq(Company, QueryID, SubQueryID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelationField item
   Description: Calls GetByID to retrieve the QueryRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelationFields(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySortBies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuerySortBies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySortBies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySortBies",headers=creds) as resp:
           return await resp.json()

async def get_QuerySortBies_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySortBy item
   Description: Calls GetByID to retrieve the QuerySortBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortBy
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySortByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySortBies(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryWhereItems(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryWhereItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryWhereItems
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryWhereItems",headers=creds) as resp:
           return await resp.json()

async def get_QueryWhereItems_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryWhereItem item
   Description: Calls GetByID to retrieve the QueryWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItem
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryWhereItems(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryGroupBies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryGroupBies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryGroupBies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryGroupBies",headers=creds) as resp:
           return await resp.json()

async def get_QueryGroupBies_Company_QueryID_SubQueryID_GroupByID(Company, QueryID, SubQueryID, GroupByID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryGroupBy item
   Description: Calls GetByID to retrieve the QueryGroupBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupBy
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param GroupByID: Desc: GroupByID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryGroupByRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryGroupBies(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryTables(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables",headers=creds) as resp:
           return await resp.json()

async def get_QueryTables_Company_QueryID_SubQueryID_TableID(Company, QueryID, SubQueryID, TableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryTable item
   Description: Calls GetByID to retrieve the QueryTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTable
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFields(Company, QueryID, SubQueryID, TableID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFields1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFields",headers=creds) as resp:
           return await resp.json()

async def get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryField item
   Description: Calls GetByID to retrieve the QueryField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryField1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFunctionCalls(Company, QueryID, SubQueryID, TableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryFunctionCalls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFunctionCalls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCalls",headers=creds) as resp:
           return await resp.json()

async def get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFunctionCalls_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company, QueryID, SubQueryID, TableID, FunctionID, ParameterName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFunctionCall item
   Description: Calls GetByID to retrieve the QueryFunctionCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCall1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FunctionID: Desc: FunctionID   Required: True   Allow empty value : True
      :param ParameterName: Desc: ParameterName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCalls(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFields(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFields
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields",headers=creds) as resp:
           return await resp.json()

async def get_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryField item
   Description: Calls GetByID to retrieve the QueryField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributes(Company, QueryID, SubQueryID, TableID, FieldName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryFieldAttributes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFieldAttributes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributes",headers=creds) as resp:
           return await resp.json()

async def get_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributes_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company, QueryID, SubQueryID, TableID, FieldName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldAttribute item
   Description: Calls GetByID to retrieve the QueryFieldAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttribute1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributes(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldAttributes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryFieldAttributes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFieldAttributes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFieldAttributes",headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldAttributes_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company, QueryID, SubQueryID, TableID, FieldName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldAttribute item
   Description: Calls GetByID to retrieve the QueryFieldAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttribute
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFieldAttributes(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFunctionCalls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryFunctionCalls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFunctionCalls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFunctionCalls",headers=creds) as resp:
           return await resp.json()

async def get_QueryFunctionCalls_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company, QueryID, SubQueryID, FunctionID, ParameterName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFunctionCall item
   Description: Calls GetByID to retrieve the QueryFunctionCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCall
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param FunctionID: Desc: FunctionID   Required: True   Allow empty value : True
      :param ParameterName: Desc: ParameterName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFunctionCalls(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateFields",headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateFields_Company_QueryID_MapTableName_MapFieldName_Direction(Company, QueryID, MapTableName, MapFieldName, Direction, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateField item
   Description: Calls GetByID to retrieve the QueryUpdateField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param MapTableName: Desc: MapTableName   Required: True   Allow empty value : True
      :param MapFieldName: Desc: MapFieldName   Required: True   Allow empty value : True
      :param Direction: Desc: Direction   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateFields(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateSettings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateSettings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateSettings",headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateSettings_Company_QueryID(Company, QueryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateSetting item
   Description: Calls GetByID to retrieve the QueryUpdateSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateSettings(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryValueSetItems(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryValueSetItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryValueSetItems
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems",headers=creds) as resp:
           return await resp.json()

async def get_QueryValueSetItems_Company_QueryID_ValueSetID_ItemValue(Company, QueryID, ValueSetID, ItemValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryValueSetItem item
   Description: Calls GetByID to retrieve the QueryValueSetItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ValueSetID: Desc: ValueSetID   Required: True   Allow empty value : True
      :param ItemValue: Desc: ItemValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynamicQuery, whereClauseQueryCtrl, whereClauseQueryCtrlValues, whereClauseQueryCustomAction, whereClauseQueryExecuteSetting, whereClauseQueryParameter, whereClauseQueryReference, whereClauseQueryParameterBinding, whereClauseQuerySubQuery, whereClauseQueryRelation, whereClauseQueryRelationField, whereClauseQuerySortBy, whereClauseQueryWhereItem, whereClauseQueryGroupBy, whereClauseQueryTable, whereClauseQueryField, whereClauseQueryFunctionCall, whereClauseQueryUpdateField, whereClauseQueryUpdateSettings, whereClauseQueryValueSetItems, whereClauseQueryFieldAttribute, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method returns a list of BAQs that have a specific like field
Used by: Server\bo\EpiSearch\EpiSearch.p
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseDynamicQuery=" + whereClauseDynamicQuery
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryCtrl=" + whereClauseQueryCtrl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryCtrlValues=" + whereClauseQueryCtrlValues
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryCustomAction=" + whereClauseQueryCustomAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryExecuteSetting=" + whereClauseQueryExecuteSetting
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryParameter=" + whereClauseQueryParameter
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryReference=" + whereClauseQueryReference
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryParameterBinding=" + whereClauseQueryParameterBinding
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuerySubQuery=" + whereClauseQuerySubQuery
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryRelation=" + whereClauseQueryRelation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryRelationField=" + whereClauseQueryRelationField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuerySortBy=" + whereClauseQuerySortBy
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryWhereItem=" + whereClauseQueryWhereItem
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryGroupBy=" + whereClauseQueryGroupBy
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryTable=" + whereClauseQueryTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryField=" + whereClauseQueryField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryFunctionCall=" + whereClauseQueryFunctionCall
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryUpdateField=" + whereClauseQueryUpdateField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryUpdateSettings=" + whereClauseQueryUpdateSettings
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryValueSetItems=" + whereClauseQueryValueSetItems
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryFieldAttribute=" + whereClauseQueryFieldAttribute
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: This method returns a dataset containing definition of the query.
   OperationID: GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryEmptyResultSetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryEmptyResultSetByID
   Description: This method returns an empty result dataset. It is useful if client need information about result set schema only
   OperationID: GetQueryEmptyResultSetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryEmptyResultSetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryEmptyResultSetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryExecutionParametersByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryExecutionParametersByID
   Description: This method returns a dataset representing an query's execution parameters information
   OperationID: GetQueryExecutionParametersByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryExecutionParametersByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryExecutionParametersByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This method runs an updatable query and returns result dataset.
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDs
   Description: This method returns a dataset containing definition of queries with ids listed in parameter
   OperationID: GetByIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDsTranslated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDsTranslated
   Description: This method returns a dataset containing definition of queries with ids listed in parameter with translated labels.
   OperationID: GetByIDsTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDsTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDsTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteByID
   Description: This method run an existing query and returns an untyped dataset
   OperationID: ExecuteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Execute(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Execute
   Description: This method runs a query based on default settings.
Used by: Server\Bpm\BpmQuery.i
   OperationID: Execute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Execute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Execute_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTestQueryExecution(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTestQueryExecution
   Description: For MS SQL query checks if it is executed right now and cancel it if requested
   OperationID: CheckTestQueryExecution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTestQueryExecution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTestQueryExecution_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryExecutionPlan(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryExecutionPlan
   Description: For MS SQL query returns query execution plan
   OperationID: GetQueryExecutionPlan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryExecutionPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryExecutionPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryListFromLike(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryListFromLike
   Description: This method returns a list of BAQs that have a specific like field
Used by: Server\bo\EpiSearch\EpiSearch.p
   OperationID: GetQueryListFromLike
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryListFromLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryListFromLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryExecutionParameters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryExecutionParameters
   Description: This method returns a dataset representing an query's execution parameters information
   OperationID: GetQueryExecutionParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryExecutionParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryExecutionParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryEmptyResultSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryEmptyResultSet
   Description: This method returns an empty result dataset. It is useful if client need information about result set schema only
   OperationID: GetQueryEmptyResultSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryEmptyResultSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryEmptyResultSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryEmptyResultSetByIDAndCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryEmptyResultSetByIDAndCompany
   Description: This method returns an empty result dataset. It is useful if client need information about result set schema only
   OperationID: GetQueryEmptyResultSetByIDAndCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryEmptyResultSetByIDAndCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryEmptyResultSetByIDAndCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryResultSetMetadataByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryResultSetMetadataByID
   Description: This method returns a list of groups of attributes and values, each group per query's display field.
Attributes expose information about the field: Caption, Format, DataType, ReadOnly, etc.
   OperationID: GetQueryResultSetMetadataByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryResultSetMetadataByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryResultSetMetadataByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Analyze(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Analyze
   OperationID: Analyze
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Analyze_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Analyze_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetQueryList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryList
   Description: This method returns a list of BAQs that meet the criteria. The result can be paged.
   OperationID: Get_GetQueryList
      :param whereClause: Desc: The criteria   Required: True   Allow empty value : True
      :param pageSize: Desc: Size of the page   Required: True
      :param absolutePage: Desc: The number of the page to return   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryList_output
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListByID
   Description: This method runs an updatable query and returns result dataset.
   OperationID: GetListByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Call Update method of an updatable query and return result dataset
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateByID
   Description: Call Update method of an updatable query and return result dataset
   OperationID: UpdateByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNew
   Description: Calls GetNew method of an updatable query and return result set with added row.
   OperationID: GetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewByID
   Description: Calls GetNew method of an updatable query and return result set with added row.
   OperationID: GetNewByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FieldUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FieldUpdate
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FieldUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FieldUpdateByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FieldUpdateByID
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldUpdateByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FieldUpdateByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldUpdateByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FieldValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FieldValidate
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FieldValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FieldValidateByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FieldValidateByID
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldValidateByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FieldValidateByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldValidateByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunCustomAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunCustomAction
   Description: This method does nothing per se, but is useful if there are BPM directives
attached to the query. Directives can examine actionId value and perform some actions.
   OperationID: RunCustomAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunCustomAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunCustomAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunCustomActionByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunCustomActionByID
   Description: This method does nothing per se, but is useful if there are BPM directives
attached to the query. Directives can examine actionId value and perform some actions.
   OperationID: RunCustomActionByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunCustomActionByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunCustomActionByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDistinctValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDistinctValues
   Description: This method runs a query based on default settings and passed execution parameters and return lists of distinct values of specified fields.
   OperationID: GetDistinctValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDistinctValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDistinctValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InvalidateRuntimeQueryCache(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InvalidateRuntimeQueryCache
   Description: Removes query definition from the runtime cache. It will be reloaded on the next execution.
   OperationID: InvalidateRuntimeQueryCache
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvalidateRuntimeQueryCache_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvalidateRuntimeQueryCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDTranslated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDTranslated
   Description: This method returns a dataset containing definition of the query with translated labels.
   OperationID: GetByIDTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DynamicQueryRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryCtrlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryCtrlValuesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryCustomActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryExecuteSettingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryFieldAttributeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryFunctionCallRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryGroupByRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryParameterBindingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryParameterRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryReferenceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryRelationFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryRelationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuerySortByRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuerySubQueryRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryTableRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryUpdateFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryUpdateSettingsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryValueSetItemsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryWhereItemRow] = obj["value"]
      pass

class Ice_Tablesets_DynamicQueryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.AuthorID:str = obj["AuthorID"]
      """  AuthorID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DisplayPhrase:str = obj["DisplayPhrase"]
      """  DisplayPhrase  """  
      self.IsShared:bool = obj["IsShared"]
      """  IsShared  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.XCompany:bool = obj["XCompany"]
      """  XCompany  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  GlbCompany  """  
      self.Updatable:bool = obj["Updatable"]
      """  Updatable  """  
      self.ExtQuery:bool = obj["ExtQuery"]
      """  ExtQuery  """  
      self.ExtDatasourceName:str = obj["ExtDatasourceName"]
      """  ExtDatasourceName  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.Extension:str = obj["Extension"]
      """  Extension  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.UseLiveDB:bool = obj["UseLiveDB"]
      """  UseLiveDB  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryCtrlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ControlID:str = obj["ControlID"]
      """  GUID for control  """  
      self.DataSource:str = obj["DataSource"]
      """  Data Source  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Mandatory flag  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  Default Value  """  
      self.ControlType:str = obj["ControlType"]
      """   One of predefined constants:
Standard ? free type editor/date picker, depend on DataType.
RadioSet ? radio button set. Items are specified in QueryCtrlValues table
DropDown ? dropdown list. Items are specified in QueryCtrlValues table
DropDownBAQ ? dropdown list. Information are stored in QueryCtrlValues table with tree rows with Ids:BAQID, BAQDisplayColumn, BAQValueColumn
DropDownUserCodes - dropdown list. Information are stored in QueryCtrlValues table with one row with Id = UserCodeTypeID  """  
      self.SourceType:int = obj["SourceType"]
      """  Type of the datasource 0 - updatable field, 1 - parameter  """  
      self.ListSource:str = obj["ListSource"]
      """  ListSource  """  
      self.DisplayColumn:str = obj["DisplayColumn"]
      """  DisplayColumn  """  
      self.ValueColumn:str = obj["ValueColumn"]
      """  ValueColumn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryCtrlValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ControlID:str = obj["ControlID"]
      """  GUID for control  """  
      self.ID:str = obj["ID"]
      """  Id pof value record  """  
      self.Val:str = obj["Val"]
      """  Value  """  
      self.Seq:int = obj["Seq"]
      """  Sequence number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryCustomActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ActionID:str = obj["ActionID"]
      """  Action ID  """  
      self.ActionLabel:str = obj["ActionLabel"]
      """  Displayble text for the action  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryExecuteSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SettingID:str = obj["SettingID"]
      """  SettingID  """  
      self.SettingValue:str = obj["SettingValue"]
      """  SettingValue  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFieldAttributeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.AttributeName:str = obj["AttributeName"]
      """  AttributeName  """  
      self.Value:str = obj["Value"]
      """  Value  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsOverriden:bool = obj["IsOverriden"]
      """  Flags whether the attribute was changed by user.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.External:bool = obj["External"]
      """  External  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  IsCalculated  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldSeq:int = obj["LikeDataFieldSeq"]
      """  Like Data Field Sequence  """  
      self.Aggregation:str = obj["Aggregation"]
      """  Aggregation  """  
      self.IsGroupBy:bool = obj["IsGroupBy"]
      """  IsGroupBy  """  
      self.UseLike:bool = obj["UseLike"]
      """  Use Like  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Field Name  """  
      self.Updatable:bool = obj["Updatable"]
      """  Wheither field can be updated  """  
      self.RaiseEvent:bool = obj["RaiseEvent"]
      """  Raise event on update  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  ID of Quick Search assigned to this query field  """  
      self.DropDown:bool = obj["DropDown"]
      """  This flag tells whether this display field is used as source of distinct values for drop down list in IW  """  
      self.UpdInitExpression:str = obj["UpdInitExpression"]
      """  Initial expression for updatable field, filled on UBAQ.GetNew  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  obsolete, use Alias instead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFunctionCallRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.FunctionID:str = obj["FunctionID"]
      """  FunctionID  """  
      self.ParameterName:str = obj["ParameterName"]
      """  ParameterName  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.Value:str = obj["Value"]
      """  Value  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryGroupByRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.GroupByID:str = obj["GroupByID"]
      """  GroupByID  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryParameterBindingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ReferenceID:str = obj["ReferenceID"]
      """  ReferenceID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.MappingType:str = obj["MappingType"]
      """  MappingType  """  
      self.MappingValue:str = obj["MappingValue"]
      """  MappingValue  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryParameterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.ParameterType:str = obj["ParameterType"]
      """  Data type of the parameter  """  
      self.ParameterLabel:str = obj["ParameterLabel"]
      """  ParameterLabel  """  
      self.SkipIfEmpty:bool = obj["SkipIfEmpty"]
      """  Skip condition of parameter is not set  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryReferenceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ReferenceID:str = obj["ReferenceID"]
      """  ReferenceID  """  
      self.ReferenceName:str = obj["ReferenceName"]
      """  ReferenceName  """  
      self.RefQueryID:str = obj["RefQueryID"]
      """  RefQueryID  """  
      self.ExecType:str = obj["ExecType"]
      """  ExecType  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryRelationFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.RelationID:str = obj["RelationID"]
      """  Query Relation ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.ParentFieldName:str = obj["ParentFieldName"]
      """  Parent Field Name  """  
      self.ParentFieldDataType:str = obj["ParentFieldDataType"]
      """  ParentFieldDataType  """  
      self.ParentFieldIsExpr:bool = obj["ParentFieldIsExpr"]
      """  ParentFieldIsExpr  """  
      self.ChildFieldName:str = obj["ChildFieldName"]
      """  Child Field Name  """  
      self.ChildFieldDataType:str = obj["ChildFieldDataType"]
      """  ChildFieldDataType  """  
      self.ChildFieldIsExpr:bool = obj["ChildFieldIsExpr"]
      """  ChildFieldIsExpr  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.CompOp:str = obj["CompOp"]
      """  CompOp  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryRelationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.RelationID:str = obj["RelationID"]
      """  Query Relation ID  """  
      self.IsFK:bool = obj["IsFK"]
      """  IsFK  """  
      self.ParentTableID:str = obj["ParentTableID"]
      """  ParentTableID  """  
      self.ChildTableID:str = obj["ChildTableID"]
      """  ChildTableID  """  
      self.JoinType:str = obj["JoinType"]
      """  "Outer" = outer-join, "" = inner-join  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OuterJoin:bool = obj["OuterJoin"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuerySortByRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.IsAsc:bool = obj["IsAsc"]
      """  IsAsc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayName:str = obj["DisplayName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuerySubQueryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.IsUnion:bool = obj["IsUnion"]
      """  IsUnion  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SelectListClause:str = obj["SelectListClause"]
      """  SelectListClause  """  
      self.TopRowExpr:int = obj["TopRowExpr"]
      """  TopRowExpr  """  
      self.TopInPercent:bool = obj["TopInPercent"]
      """  TopInPercent  """  
      self.TopWithTies:bool = obj["TopWithTies"]
      """  TopWithTies  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.OrderByOffSet:str = obj["OrderByOffSet"]
      """  OrderByOffSet  """  
      self.OrderByFetch:str = obj["OrderByFetch"]
      """  OrderByFetch  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.TableType:str = obj["TableType"]
      """  TableType  """  
      self.IsSummaryTable:bool = obj["IsSummaryTable"]
      """  Summary Table flag  """  
      self.IsVisibleInDesigner:bool = obj["IsVisibleInDesigner"]
      """  IsVisibleInDesigner  """  
      self.Modifiers:str = obj["Modifiers"]
      """  Modifiers  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PivotFunction:str = obj["PivotFunction"]
      """  PivotFunction  """  
      self.PivotDataType:str = obj["PivotDataType"]
      """  PivotDataType  """  
      self.PivotFieldFormat:str = obj["PivotFieldFormat"]
      """  PivotFieldFormat  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryUpdateFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.MapTableName:str = obj["MapTableName"]
      """  MapTableName  """  
      self.MapFieldName:str = obj["MapFieldName"]
      """  MapFieldName  """  
      self.Direction:bool = obj["Direction"]
      """  Direction  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.IsKeyField:bool = obj["IsKeyField"]
      """  IsKeyField  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NetDataType:str = obj["NetDataType"]
      """  NetDataType  """  
      self.DataType:str = obj["DataType"]
      """  Shows field data type - taken from zDataField  """  
      self.QualifiedName:str = obj["QualifiedName"]
      """  DBTableName + "." + DBFieldName  """  
      self.Required:bool = obj["Required"]
      """  Shows if field is required - taken from zDataField  """  
      self.Description:str = obj["Description"]
      """  Shows field description - taken from zDataField  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryUpdateSettingsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.AllowAddNew:bool = obj["AllowAddNew"]
      """  AllowAddNew  """  
      self.AddNewLabel:str = obj["AddNewLabel"]
      """  AddNewLabel  """  
      self.SupportMDR:bool = obj["SupportMDR"]
      """  SupportMDR  """  
      self.UpdatableType:str = obj["UpdatableType"]
      """  UpdatableType  """  
      self.UpdatableBO:str = obj["UpdatableBO"]
      """  UpdatableBO  """  
      self.BOSystemCode:str = obj["BOSystemCode"]
      """  BOSystemCode  """  
      self.UpdateMethod:str = obj["UpdateMethod"]
      """  UpdateMethod  """  
      self.SCUrl:str = obj["SCUrl"]
      """  SCUrl  """  
      self.SCWorkflow:str = obj["SCWorkflow"]
      """  SCWorkflow  """  
      self.SCCtxUser:str = obj["SCCtxUser"]
      """  SCCtxUser  """  
      self.SCCtxPwd:str = obj["SCCtxPwd"]
      """  SCCtxPwd  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SCUserID:str = obj["SCUserID"]
      """  SCUserID  """  
      self.SCPassword:str = obj["SCPassword"]
      """  SCPassword  """  
      self.SCCtxUrl:str = obj["SCCtxUrl"]
      """  SCCtxUrl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryValueSetItemsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ValueSetID:str = obj["ValueSetID"]
      """  ID of set of values. Is referenced by QueryWhereItem record for example.  """  
      self.ItemValue:str = obj["ItemValue"]
      """  Item Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryWhereItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.CriteriaID:str = obj["CriteriaID"]
      """  CriteriaID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.AndOr:str = obj["AndOr"]
      self.Neg:bool = obj["Neg"]
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.IsConst:bool = obj["IsConst"]
      """  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  """  
      self.CriteriaType:int = obj["CriteriaType"]
      """  CriteriaType  """  
      self.ToTableID:str = obj["ToTableID"]
      """  ToTableID  """  
      self.ToFieldName:str = obj["ToFieldName"]
      self.ToDataType:str = obj["ToDataType"]
      """  ToDataType  """  
      self.RValue:str = obj["RValue"]
      self.ExtSecurity:bool = obj["ExtSecurity"]
      """  ExtSecurity  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Analyze_input:
   """ Required : 
   queryDS
   executionParams
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      self.executionParams:list[Ice_Tablesets_QueryExecutionTableset] = obj["executionParams"]
      pass

class Analyze_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessages:list = obj[any]
      pass

      """  output parameters  """  

class CheckTestQueryExecution_input:
   """ Required : 
   executionToken
   extDsn
   cancelExecution
   """  
   def __init__(self, obj):
      self.executionToken:str = obj["executionToken"]
      self.extDsn:str = obj["extDsn"]
      """  dsn for external queries  """  
      self.cancelExecution:bool = obj["cancelExecution"]
      pass

class CheckTestQueryExecution_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExecuteByID_input:
   """ Required : 
   queryID
   executionParams
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The current Query ID  """  
      self.executionParams:list[Ice_Tablesets_QueryExecutionTableset] = obj["executionParams"]
      pass

class ExecuteByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result of the query  """  
      pass

class Execute_input:
   """ Required : 
   queryDS
   executionParams
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      self.executionParams:list[Ice_Tablesets_QueryExecutionTableset] = obj["executionParams"]
      pass

class Execute_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

class FieldUpdateByID_input:
   """ Required : 
   queryID
   fieldName
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.fieldName:str = obj["fieldName"]
      """  Name of an updatable field  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

class FieldUpdateByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

class FieldUpdate_input:
   """ Required : 
   queryDS
   fieldName
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      self.fieldName:str = obj["fieldName"]
      """  Name of an updatable field  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

class FieldUpdate_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

class FieldValidateByID_input:
   """ Required : 
   queryID
   fieldName
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.fieldName:str = obj["fieldName"]
      """  Name of an updatable field  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class FieldValidateByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

   def parameters(self, obj):
      self.isValid:bool = obj["isValid"]
      pass

      """  output parameters  """  

class FieldValidate_input:
   """ Required : 
   queryDS
   fieldName
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      self.fieldName:str = obj["fieldName"]
      """  Name of an updatable field  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class FieldValidate_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

   def parameters(self, obj):
      self.isValid:bool = obj["isValid"]
      pass

      """  output parameters  """  

class GetByIDTranslated_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Query id to load definition  """  
      pass

class GetByIDTranslated_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Query id to load definition.  """  
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryTableset] = obj["returnObj"]
      pass

class GetByIDsTranslated_input:
   """ Required : 
   queryIDList
   """  
   def __init__(self, obj):
      self.queryIDList:str = obj["queryIDList"]
      """  List of query ids to load definition  """  
      pass

class GetByIDsTranslated_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryTableset] = obj["returnObj"]
      pass

class GetByIDs_input:
   """ Required : 
   queryIDList
   """  
   def __init__(self, obj):
      self.queryIDList:str = obj["queryIDList"]
      """  List of query ids to load definition  """  
      pass

class GetByIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryTableset] = obj["returnObj"]
      pass

class GetDistinctValues_input:
   """ Required : 
   queryID
   executionParams
   distinctFields
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query ID  """  
      self.executionParams:list[Ice_Tablesets_QueryExecutionTableset] = obj["executionParams"]
      self.distinctFields:str = obj["distinctFields"]
      """  List of query display fields distinct values of which should be returned  """  
      pass

class GetDistinctValues_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

class GetListByID_input:
   """ Required : 
   queryID
   executionParams
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Query's id to execute  """  
      self.executionParams:list[Ice_Tablesets_QueryExecutionTableset] = obj["executionParams"]
      self.pageSize:int = obj["pageSize"]
      """  Number of records in a page. 0 means you don't want paging  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Number of page to return. 1 should be set by default  """  
      pass

class GetListByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

   def parameters(self, obj):
      self.hasMorePage:bool = obj["hasMorePage"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   queryDS
   executionParams
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      self.executionParams:list[Ice_Tablesets_QueryExecutionTableset] = obj["executionParams"]
      self.pageSize:int = obj["pageSize"]
      """  Number of records in a page. 0 means you don't want paging  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Number of page to return. 1 should be set by default  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

   def parameters(self, obj):
      self.hasMorePage:bool = obj["hasMorePage"]
      pass

      """  output parameters  """  

class GetNewByID_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      pass

class GetNewByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Result of method call. A new expected to be added to results table  """  
      pass

class GetNew_input:
   """ Required : 
   queryDS
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      pass

class GetNew_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Result of method call. A new expected to be added to results table  """  
      pass

class GetQueryEmptyResultSetByIDAndCompany_input:
   """ Required : 
   queryID
   companyID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query ID  """  
      self.companyID:str = obj["companyID"]
      """  The query's Company ID  """  
      pass

class GetQueryEmptyResultSetByIDAndCompany_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the empty dataset representing the query result  """  
      pass

class GetQueryEmptyResultSetByID_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query ID  """  
      pass

class GetQueryEmptyResultSetByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the empty dataset representing the query result  """  
      pass

class GetQueryEmptyResultSet_input:
   """ Required : 
   queryDS
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      pass

class GetQueryEmptyResultSet_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the empty dataset representing the query result  """  
      pass

class GetQueryExecutionParametersByID_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query ID  """  
      pass

class GetQueryExecutionParametersByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QueryExecutionTableset] = obj["returnObj"]
      pass

class GetQueryExecutionParameters_input:
   """ Required : 
   queryDS
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      pass

class GetQueryExecutionParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QueryExecutionTableset] = obj["returnObj"]
      pass

class GetQueryExecutionPlan_input:
   """ Required : 
   executionToken
   extDsn
   """  
   def __init__(self, obj):
      self.executionToken:str = obj["executionToken"]
      self.extDsn:str = obj["extDsn"]
      """  dsn for external queries  """  
      pass

class GetQueryExecutionPlan_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetQueryListFromLike_input:
   """ Required : 
   likeTableName
   likeFieldName
   """  
   def __init__(self, obj):
      self.likeTableName:str = obj["likeTableName"]
      """  The table name of the like field  """  
      self.likeFieldName:str = obj["likeFieldName"]
      """  The field name of the like field  """  
      pass

class GetQueryListFromLike_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryListTableset] = obj["returnObj"]
      pass

class GetQueryList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of the page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The number of the page to return  """  
      pass

class GetQueryList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetQueryResultSetMetadataByID_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query ID  """  
      pass

class GetQueryResultSetMetadataByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_DynamicQuery_ResultFieldMetadata] = obj["returnObj"]
      """  Returns the attributes and values grouped by query's display fields  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseDynamicQuery
   whereClauseQueryCtrl
   whereClauseQueryCtrlValues
   whereClauseQueryCustomAction
   whereClauseQueryExecuteSetting
   whereClauseQueryParameter
   whereClauseQueryReference
   whereClauseQueryParameterBinding
   whereClauseQuerySubQuery
   whereClauseQueryRelation
   whereClauseQueryRelationField
   whereClauseQuerySortBy
   whereClauseQueryWhereItem
   whereClauseQueryGroupBy
   whereClauseQueryTable
   whereClauseQueryField
   whereClauseQueryFunctionCall
   whereClauseQueryUpdateField
   whereClauseQueryUpdateSettings
   whereClauseQueryValueSetItems
   whereClauseQueryFieldAttribute
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynamicQuery:str = obj["whereClauseDynamicQuery"]
      self.whereClauseQueryCtrl:str = obj["whereClauseQueryCtrl"]
      self.whereClauseQueryCtrlValues:str = obj["whereClauseQueryCtrlValues"]
      self.whereClauseQueryCustomAction:str = obj["whereClauseQueryCustomAction"]
      self.whereClauseQueryExecuteSetting:str = obj["whereClauseQueryExecuteSetting"]
      self.whereClauseQueryParameter:str = obj["whereClauseQueryParameter"]
      self.whereClauseQueryReference:str = obj["whereClauseQueryReference"]
      self.whereClauseQueryParameterBinding:str = obj["whereClauseQueryParameterBinding"]
      self.whereClauseQuerySubQuery:str = obj["whereClauseQuerySubQuery"]
      self.whereClauseQueryRelation:str = obj["whereClauseQueryRelation"]
      self.whereClauseQueryRelationField:str = obj["whereClauseQueryRelationField"]
      self.whereClauseQuerySortBy:str = obj["whereClauseQuerySortBy"]
      self.whereClauseQueryWhereItem:str = obj["whereClauseQueryWhereItem"]
      self.whereClauseQueryGroupBy:str = obj["whereClauseQueryGroupBy"]
      self.whereClauseQueryTable:str = obj["whereClauseQueryTable"]
      self.whereClauseQueryField:str = obj["whereClauseQueryField"]
      self.whereClauseQueryFunctionCall:str = obj["whereClauseQueryFunctionCall"]
      self.whereClauseQueryUpdateField:str = obj["whereClauseQueryUpdateField"]
      self.whereClauseQueryUpdateSettings:str = obj["whereClauseQueryUpdateSettings"]
      self.whereClauseQueryValueSetItems:str = obj["whereClauseQueryValueSetItems"]
      self.whereClauseQueryFieldAttribute:str = obj["whereClauseQueryFieldAttribute"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BO_DynamicQuery_ResultFieldMetadata:
   def __init__(self, obj):
      self.alias:str = obj["alias"]
      self.typeName:str = obj["typeName"]
      self.seq:int = obj["seq"]
      self.caption:str = obj["caption"]
      self.format:str = obj["format"]
      self.like:str = obj["like"]
      self.readOnly:bool = obj["readOnly"]
      self.required:bool = obj["required"]
      self.attributes      #schema had no properties on an object.
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

class Ice_Tablesets_DynamicQueryListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.AuthorID:str = obj["AuthorID"]
      """  AuthorID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsShared:bool = obj["IsShared"]
      """  IsShared  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.XCompany:bool = obj["XCompany"]
      """  XCompany  """  
      self.Updatable:bool = obj["Updatable"]
      """  Updatable  """  
      self.ExtQuery:bool = obj["ExtQuery"]
      """  ExtQuery  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DynamicQueryListTableset:
   def __init__(self, obj):
      self.DynamicQueryList:list[Ice_Tablesets_DynamicQueryListRow] = obj["DynamicQueryList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DynamicQueryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.AuthorID:str = obj["AuthorID"]
      """  AuthorID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DisplayPhrase:str = obj["DisplayPhrase"]
      """  DisplayPhrase  """  
      self.IsShared:bool = obj["IsShared"]
      """  IsShared  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.XCompany:bool = obj["XCompany"]
      """  XCompany  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  GlbCompany  """  
      self.Updatable:bool = obj["Updatable"]
      """  Updatable  """  
      self.ExtQuery:bool = obj["ExtQuery"]
      """  ExtQuery  """  
      self.ExtDatasourceName:str = obj["ExtDatasourceName"]
      """  ExtDatasourceName  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.Extension:str = obj["Extension"]
      """  Extension  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.UseLiveDB:bool = obj["UseLiveDB"]
      """  UseLiveDB  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DynamicQueryTableset:
   def __init__(self, obj):
      self.DynamicQuery:list[Ice_Tablesets_DynamicQueryRow] = obj["DynamicQuery"]
      self.QueryCtrl:list[Ice_Tablesets_QueryCtrlRow] = obj["QueryCtrl"]
      self.QueryCtrlValues:list[Ice_Tablesets_QueryCtrlValuesRow] = obj["QueryCtrlValues"]
      self.QueryCustomAction:list[Ice_Tablesets_QueryCustomActionRow] = obj["QueryCustomAction"]
      self.QueryExecuteSetting:list[Ice_Tablesets_QueryExecuteSettingRow] = obj["QueryExecuteSetting"]
      self.QueryParameter:list[Ice_Tablesets_QueryParameterRow] = obj["QueryParameter"]
      self.QueryReference:list[Ice_Tablesets_QueryReferenceRow] = obj["QueryReference"]
      self.QueryParameterBinding:list[Ice_Tablesets_QueryParameterBindingRow] = obj["QueryParameterBinding"]
      self.QuerySubQuery:list[Ice_Tablesets_QuerySubQueryRow] = obj["QuerySubQuery"]
      self.QueryRelation:list[Ice_Tablesets_QueryRelationRow] = obj["QueryRelation"]
      self.QueryRelationField:list[Ice_Tablesets_QueryRelationFieldRow] = obj["QueryRelationField"]
      self.QuerySortBy:list[Ice_Tablesets_QuerySortByRow] = obj["QuerySortBy"]
      self.QueryWhereItem:list[Ice_Tablesets_QueryWhereItemRow] = obj["QueryWhereItem"]
      self.QueryGroupBy:list[Ice_Tablesets_QueryGroupByRow] = obj["QueryGroupBy"]
      self.QueryTable:list[Ice_Tablesets_QueryTableRow] = obj["QueryTable"]
      self.QueryField:list[Ice_Tablesets_QueryFieldRow] = obj["QueryField"]
      self.QueryFieldAttribute:list[Ice_Tablesets_QueryFieldAttributeRow] = obj["QueryFieldAttribute"]
      self.QueryFunctionCall:list[Ice_Tablesets_QueryFunctionCallRow] = obj["QueryFunctionCall"]
      self.QueryUpdateField:list[Ice_Tablesets_QueryUpdateFieldRow] = obj["QueryUpdateField"]
      self.QueryUpdateSettings:list[Ice_Tablesets_QueryUpdateSettingsRow] = obj["QueryUpdateSettings"]
      self.QueryValueSetItems:list[Ice_Tablesets_QueryValueSetItemsRow] = obj["QueryValueSetItems"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExecutionFilterRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Neg:bool = obj["Neg"]
      self.CompOp:str = obj["CompOp"]
      self.RValue:str = obj["RValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExecutionParameterRow:
   def __init__(self, obj):
      self.ParameterID:str = obj["ParameterID"]
      self.ParameterValue:str = obj["ParameterValue"]
      self.ValueType:str = obj["ValueType"]
      self.IsEmpty:bool = obj["IsEmpty"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExecutionSettingRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      """  name of setting  """  
      self.Value:str = obj["Value"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExecutionValueSetItemsRow:
   def __init__(self, obj):
      self.ValueSetID:str = obj["ValueSetID"]
      self.ItemValue:str = obj["ItemValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryCtrlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ControlID:str = obj["ControlID"]
      """  GUID for control  """  
      self.DataSource:str = obj["DataSource"]
      """  Data Source  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Mandatory flag  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  Default Value  """  
      self.ControlType:str = obj["ControlType"]
      """   One of predefined constants:
Standard ? free type editor/date picker, depend on DataType.
RadioSet ? radio button set. Items are specified in QueryCtrlValues table
DropDown ? dropdown list. Items are specified in QueryCtrlValues table
DropDownBAQ ? dropdown list. Information are stored in QueryCtrlValues table with tree rows with Ids:BAQID, BAQDisplayColumn, BAQValueColumn
DropDownUserCodes - dropdown list. Information are stored in QueryCtrlValues table with one row with Id = UserCodeTypeID  """  
      self.SourceType:int = obj["SourceType"]
      """  Type of the datasource 0 - updatable field, 1 - parameter  """  
      self.ListSource:str = obj["ListSource"]
      """  ListSource  """  
      self.DisplayColumn:str = obj["DisplayColumn"]
      """  DisplayColumn  """  
      self.ValueColumn:str = obj["ValueColumn"]
      """  ValueColumn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryCtrlValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ControlID:str = obj["ControlID"]
      """  GUID for control  """  
      self.ID:str = obj["ID"]
      """  Id pof value record  """  
      self.Val:str = obj["Val"]
      """  Value  """  
      self.Seq:int = obj["Seq"]
      """  Sequence number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryCustomActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ActionID:str = obj["ActionID"]
      """  Action ID  """  
      self.ActionLabel:str = obj["ActionLabel"]
      """  Displayble text for the action  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryExecuteSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SettingID:str = obj["SettingID"]
      """  SettingID  """  
      self.SettingValue:str = obj["SettingValue"]
      """  SettingValue  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryExecutionTableset:
   def __init__(self, obj):
      self.ExecutionFilter:list[Ice_Tablesets_ExecutionFilterRow] = obj["ExecutionFilter"]
      self.ExecutionParameter:list[Ice_Tablesets_ExecutionParameterRow] = obj["ExecutionParameter"]
      self.ExecutionSetting:list[Ice_Tablesets_ExecutionSettingRow] = obj["ExecutionSetting"]
      self.ExecutionValueSetItems:list[Ice_Tablesets_ExecutionValueSetItemsRow] = obj["ExecutionValueSetItems"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QueryFieldAttributeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.AttributeName:str = obj["AttributeName"]
      """  AttributeName  """  
      self.Value:str = obj["Value"]
      """  Value  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsOverriden:bool = obj["IsOverriden"]
      """  Flags whether the attribute was changed by user.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.External:bool = obj["External"]
      """  External  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  IsCalculated  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldSeq:int = obj["LikeDataFieldSeq"]
      """  Like Data Field Sequence  """  
      self.Aggregation:str = obj["Aggregation"]
      """  Aggregation  """  
      self.IsGroupBy:bool = obj["IsGroupBy"]
      """  IsGroupBy  """  
      self.UseLike:bool = obj["UseLike"]
      """  Use Like  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Field Name  """  
      self.Updatable:bool = obj["Updatable"]
      """  Wheither field can be updated  """  
      self.RaiseEvent:bool = obj["RaiseEvent"]
      """  Raise event on update  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  ID of Quick Search assigned to this query field  """  
      self.DropDown:bool = obj["DropDown"]
      """  This flag tells whether this display field is used as source of distinct values for drop down list in IW  """  
      self.UpdInitExpression:str = obj["UpdInitExpression"]
      """  Initial expression for updatable field, filled on UBAQ.GetNew  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  obsolete, use Alias instead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFunctionCallRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.FunctionID:str = obj["FunctionID"]
      """  FunctionID  """  
      self.ParameterName:str = obj["ParameterName"]
      """  ParameterName  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.Value:str = obj["Value"]
      """  Value  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryGroupByRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.GroupByID:str = obj["GroupByID"]
      """  GroupByID  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryParameterBindingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ReferenceID:str = obj["ReferenceID"]
      """  ReferenceID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.MappingType:str = obj["MappingType"]
      """  MappingType  """  
      self.MappingValue:str = obj["MappingValue"]
      """  MappingValue  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryParameterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.ParameterType:str = obj["ParameterType"]
      """  Data type of the parameter  """  
      self.ParameterLabel:str = obj["ParameterLabel"]
      """  ParameterLabel  """  
      self.SkipIfEmpty:bool = obj["SkipIfEmpty"]
      """  Skip condition of parameter is not set  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryReferenceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ReferenceID:str = obj["ReferenceID"]
      """  ReferenceID  """  
      self.ReferenceName:str = obj["ReferenceName"]
      """  ReferenceName  """  
      self.RefQueryID:str = obj["RefQueryID"]
      """  RefQueryID  """  
      self.ExecType:str = obj["ExecType"]
      """  ExecType  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryRelationFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.RelationID:str = obj["RelationID"]
      """  Query Relation ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.ParentFieldName:str = obj["ParentFieldName"]
      """  Parent Field Name  """  
      self.ParentFieldDataType:str = obj["ParentFieldDataType"]
      """  ParentFieldDataType  """  
      self.ParentFieldIsExpr:bool = obj["ParentFieldIsExpr"]
      """  ParentFieldIsExpr  """  
      self.ChildFieldName:str = obj["ChildFieldName"]
      """  Child Field Name  """  
      self.ChildFieldDataType:str = obj["ChildFieldDataType"]
      """  ChildFieldDataType  """  
      self.ChildFieldIsExpr:bool = obj["ChildFieldIsExpr"]
      """  ChildFieldIsExpr  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.CompOp:str = obj["CompOp"]
      """  CompOp  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryRelationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.RelationID:str = obj["RelationID"]
      """  Query Relation ID  """  
      self.IsFK:bool = obj["IsFK"]
      """  IsFK  """  
      self.ParentTableID:str = obj["ParentTableID"]
      """  ParentTableID  """  
      self.ChildTableID:str = obj["ChildTableID"]
      """  ChildTableID  """  
      self.JoinType:str = obj["JoinType"]
      """  "Outer" = outer-join, "" = inner-join  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OuterJoin:bool = obj["OuterJoin"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuerySortByRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.IsAsc:bool = obj["IsAsc"]
      """  IsAsc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayName:str = obj["DisplayName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuerySubQueryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.IsUnion:bool = obj["IsUnion"]
      """  IsUnion  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SelectListClause:str = obj["SelectListClause"]
      """  SelectListClause  """  
      self.TopRowExpr:int = obj["TopRowExpr"]
      """  TopRowExpr  """  
      self.TopInPercent:bool = obj["TopInPercent"]
      """  TopInPercent  """  
      self.TopWithTies:bool = obj["TopWithTies"]
      """  TopWithTies  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.OrderByOffSet:str = obj["OrderByOffSet"]
      """  OrderByOffSet  """  
      self.OrderByFetch:str = obj["OrderByFetch"]
      """  OrderByFetch  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.TableType:str = obj["TableType"]
      """  TableType  """  
      self.IsSummaryTable:bool = obj["IsSummaryTable"]
      """  Summary Table flag  """  
      self.IsVisibleInDesigner:bool = obj["IsVisibleInDesigner"]
      """  IsVisibleInDesigner  """  
      self.Modifiers:str = obj["Modifiers"]
      """  Modifiers  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PivotFunction:str = obj["PivotFunction"]
      """  PivotFunction  """  
      self.PivotDataType:str = obj["PivotDataType"]
      """  PivotDataType  """  
      self.PivotFieldFormat:str = obj["PivotFieldFormat"]
      """  PivotFieldFormat  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryUpdateFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.MapTableName:str = obj["MapTableName"]
      """  MapTableName  """  
      self.MapFieldName:str = obj["MapFieldName"]
      """  MapFieldName  """  
      self.Direction:bool = obj["Direction"]
      """  Direction  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.IsKeyField:bool = obj["IsKeyField"]
      """  IsKeyField  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NetDataType:str = obj["NetDataType"]
      """  NetDataType  """  
      self.DataType:str = obj["DataType"]
      """  Shows field data type - taken from zDataField  """  
      self.QualifiedName:str = obj["QualifiedName"]
      """  DBTableName + "." + DBFieldName  """  
      self.Required:bool = obj["Required"]
      """  Shows if field is required - taken from zDataField  """  
      self.Description:str = obj["Description"]
      """  Shows field description - taken from zDataField  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryUpdateSettingsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.AllowAddNew:bool = obj["AllowAddNew"]
      """  AllowAddNew  """  
      self.AddNewLabel:str = obj["AddNewLabel"]
      """  AddNewLabel  """  
      self.SupportMDR:bool = obj["SupportMDR"]
      """  SupportMDR  """  
      self.UpdatableType:str = obj["UpdatableType"]
      """  UpdatableType  """  
      self.UpdatableBO:str = obj["UpdatableBO"]
      """  UpdatableBO  """  
      self.BOSystemCode:str = obj["BOSystemCode"]
      """  BOSystemCode  """  
      self.UpdateMethod:str = obj["UpdateMethod"]
      """  UpdateMethod  """  
      self.SCUrl:str = obj["SCUrl"]
      """  SCUrl  """  
      self.SCWorkflow:str = obj["SCWorkflow"]
      """  SCWorkflow  """  
      self.SCCtxUser:str = obj["SCCtxUser"]
      """  SCCtxUser  """  
      self.SCCtxPwd:str = obj["SCCtxPwd"]
      """  SCCtxPwd  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SCUserID:str = obj["SCUserID"]
      """  SCUserID  """  
      self.SCPassword:str = obj["SCPassword"]
      """  SCPassword  """  
      self.SCCtxUrl:str = obj["SCCtxUrl"]
      """  SCCtxUrl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryValueSetItemsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.ValueSetID:str = obj["ValueSetID"]
      """  ID of set of values. Is referenced by QueryWhereItem record for example.  """  
      self.ItemValue:str = obj["ItemValue"]
      """  Item Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryWhereItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.CriteriaID:str = obj["CriteriaID"]
      """  CriteriaID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence Number  """  
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.AndOr:str = obj["AndOr"]
      self.Neg:bool = obj["Neg"]
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.IsConst:bool = obj["IsConst"]
      """  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  """  
      self.CriteriaType:int = obj["CriteriaType"]
      """  CriteriaType  """  
      self.ToTableID:str = obj["ToTableID"]
      """  ToTableID  """  
      self.ToFieldName:str = obj["ToFieldName"]
      self.ToDataType:str = obj["ToDataType"]
      """  ToDataType  """  
      self.RValue:str = obj["RValue"]
      self.ExtSecurity:bool = obj["ExtSecurity"]
      """  ExtSecurity  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class InvalidateRuntimeQueryCache_input:
   """ Required : 
   queryID
   companyID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Query id to remove from cache. Leave empty to clear cache completely.  """  
      self.companyID:str = obj["companyID"]
      """  Company Id from query definition.  """  
      pass

class InvalidateRuntimeQueryCache_output:
   def __init__(self, obj):
      pass

class RunCustomActionByID_input:
   """ Required : 
   queryID
   actionID
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.actionID:str = obj["actionID"]
      """  An action id  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class RunCustomActionByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class RunCustomAction_input:
   """ Required : 
   queryDS
   actionID
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      self.actionID:str = obj["actionID"]
      """  An action id  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class RunCustomAction_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class UpdateByID_input:
   """ Required : 
   queryID
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset  """  
      pass

class UpdateByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Result of Update method call. Usually this is incoming query result dataset with some changes  """  
      pass

class Update_input:
   """ Required : 
   queryDS
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryDS:list[Ice_Tablesets_DynamicQueryTableset] = obj["queryDS"]
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset  """  
      pass

class Update_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Result of Update method call. Usually this is incoming query result dataset with some changes  """  
      pass

