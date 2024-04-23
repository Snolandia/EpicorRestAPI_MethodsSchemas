import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BAQDesignerSvc
# Description: BAQ designer service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQDesigners
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DynamicQueryDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners",headers=creds) as resp:
           return await resp.json()

async def post_BAQDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID(Company, QueryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQDesigner item
   Description: Calls GetByID to retrieve the BAQDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQDesigners_Company_QueryID(Company, QueryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQDesigner for the service
   Description: Calls UpdateExt to update BAQDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQDesigners_Company_QueryID(Company, QueryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQDesigner item
   Description: Call UpdateExt to delete BAQDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryCtrlDesigners(Company, QueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrlDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrlDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCtrlDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryCtrlDesigners_Company_QueryID_ControlID(Company, QueryID, ControlID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrlDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryCustomActionDesigners(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryCustomActionDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCustomActionDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCustomActionDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryCustomActionDesigners_Company_QueryID_ActionID(Company, QueryID, ActionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCustomActionDesigner item
   Description: Calls GetByID to retrieve the QueryCustomActionDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomActionDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryExecuteSettingDesigners(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryExecuteSettingDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryExecuteSettingDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryExecuteSettingDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company, QueryID, SettingID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryExecuteSettingDesigner item
   Description: Calls GetByID to retrieve the QueryExecuteSettingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSettingDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SettingID: Desc: SettingID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryParameterDesigners(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryParameterDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameterDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryParameterDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryParameterDesigners_Company_QueryID_ParameterID(Company, QueryID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameterDesigner item
   Description: Calls GetByID to retrieve the QueryParameterDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryReferenceDesigners(Company, QueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryReferenceDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryReferenceDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryReferenceDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company, QueryID, ReferenceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryReferenceDesigner item
   Description: Calls GetByID to retrieve the QueryReferenceDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReferenceDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QuerySubQueryDesigners(Company, QueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuerySubQueryDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySubQueryDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QuerySubQueryDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySubQueryDesigner item
   Description: Calls GetByID to retrieve the QuerySubQueryDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQueryDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryUpdateFieldDesigners(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateFieldDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateFieldDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateFieldDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company, QueryID, MapTableName, MapFieldName, Direction, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateFieldDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateFieldDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryUpdateSettingsDesigners(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateSettingsDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateSettingsDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateSettingsDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryUpdateSettingsDesigners_Company_QueryID(Company, QueryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSettingsDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryValueSetItemsDesigners(Company, QueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryValueSetItemsDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryValueSetItemsDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryValueSetItemsDesigners",headers=creds) as resp:
           return await resp.json()

async def get_BAQDesigners_Company_QueryID_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company, QueryID, ValueSetID, ItemValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryValueSetItemsDesigner item
   Description: Calls GetByID to retrieve the QueryValueSetItemsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItemsDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ValueSetID: Desc: ValueSetID   Required: True   Allow empty value : True
      :param ItemValue: Desc: ItemValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlDesigners(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrlDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrlDesigners
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryCtrlDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryCtrlDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlDesigners_Company_QueryID_ControlID(Company, QueryID, ControlID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrlDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryCtrlDesigners_Company_QueryID_ControlID(Company, QueryID, ControlID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryCtrlDesigner for the service
   Description: Calls UpdateExt to update QueryCtrlDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryCtrlDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryCtrlDesigners_Company_QueryID_ControlID(Company, QueryID, ControlID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryCtrlDesigner item
   Description: Call UpdateExt to delete QueryCtrlDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryCtrlDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlDesigners_Company_QueryID_ControlID_QueryCtrlValuesDesigners(Company, QueryID, ControlID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrlValuesDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrlValuesDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValuesDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlDesigners_Company_QueryID_ControlID_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company, QueryID, ControlID, ID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrlValuesDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlValuesDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValuesDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param ID: Desc: ID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlValuesDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrlValuesDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrlValuesDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryCtrlValuesDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryCtrlValuesDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company, QueryID, ControlID, ID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCtrlValuesDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlValuesDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValuesDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param ID: Desc: ID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company, QueryID, ControlID, ID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryCtrlValuesDesigner for the service
   Description: Calls UpdateExt to update QueryCtrlValuesDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryCtrlValuesDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param ID: Desc: ID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company, QueryID, ControlID, ID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryCtrlValuesDesigner item
   Description: Call UpdateExt to delete QueryCtrlValuesDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryCtrlValuesDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ControlID: Desc: ControlID   Required: True   Allow empty value : True
      :param ID: Desc: ID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryCustomActionDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryCustomActionDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCustomActionDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryCustomActionDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryCustomActionDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryCustomActionDesigners_Company_QueryID_ActionID(Company, QueryID, ActionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryCustomActionDesigner item
   Description: Calls GetByID to retrieve the QueryCustomActionDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomActionDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryCustomActionDesigners_Company_QueryID_ActionID(Company, QueryID, ActionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryCustomActionDesigner for the service
   Description: Calls UpdateExt to update QueryCustomActionDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryCustomActionDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryCustomActionDesigners_Company_QueryID_ActionID(Company, QueryID, ActionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryCustomActionDesigner item
   Description: Call UpdateExt to delete QueryCustomActionDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryCustomActionDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryExecuteSettingDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryExecuteSettingDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryExecuteSettingDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryExecuteSettingDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryExecuteSettingDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company, QueryID, SettingID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryExecuteSettingDesigner item
   Description: Calls GetByID to retrieve the QueryExecuteSettingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSettingDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SettingID: Desc: SettingID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company, QueryID, SettingID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryExecuteSettingDesigner for the service
   Description: Calls UpdateExt to update QueryExecuteSettingDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryExecuteSettingDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SettingID: Desc: SettingID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company, QueryID, SettingID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryExecuteSettingDesigner item
   Description: Call UpdateExt to delete QueryExecuteSettingDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryExecuteSettingDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SettingID: Desc: SettingID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryParameterDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryParameterDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameterDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryParameterDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryParameterDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryParameterDesigners_Company_QueryID_ParameterID(Company, QueryID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameterDesigner item
   Description: Calls GetByID to retrieve the QueryParameterDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryParameterDesigners_Company_QueryID_ParameterID(Company, QueryID, ParameterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryParameterDesigner for the service
   Description: Calls UpdateExt to update QueryParameterDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryParameterDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryParameterDesigners_Company_QueryID_ParameterID(Company, QueryID, ParameterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryParameterDesigner item
   Description: Call UpdateExt to delete QueryParameterDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryParameterDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryReferenceDesigners(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryReferenceDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryReferenceDesigners
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryReferenceDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryReferenceDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company, QueryID, ReferenceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryReferenceDesigner item
   Description: Calls GetByID to retrieve the QueryReferenceDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReferenceDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company, QueryID, ReferenceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryReferenceDesigner for the service
   Description: Calls UpdateExt to update QueryReferenceDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryReferenceDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company, QueryID, ReferenceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryReferenceDesigner item
   Description: Call UpdateExt to delete QueryReferenceDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryReferenceDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryReferenceDesigners_Company_QueryID_ReferenceID_QueryParameterBindingDesigners(Company, QueryID, ReferenceID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryParameterBindingDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameterBindingDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindingDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QueryReferenceDesigners_Company_QueryID_ReferenceID_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company, QueryID, ReferenceID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameterBindingDesigner item
   Description: Calls GetByID to retrieve the QueryParameterBindingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBindingDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryParameterBindingDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryParameterBindingDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameterBindingDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryParameterBindingDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryParameterBindingDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company, QueryID, ReferenceID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryParameterBindingDesigner item
   Description: Calls GetByID to retrieve the QueryParameterBindingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBindingDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company, QueryID, ReferenceID, ParameterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryParameterBindingDesigner for the service
   Description: Calls UpdateExt to update QueryParameterBindingDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryParameterBindingDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company, QueryID, ReferenceID, ParameterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryParameterBindingDesigner item
   Description: Call UpdateExt to delete QueryParameterBindingDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryParameterBindingDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ReferenceID: Desc: ReferenceID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuerySubQueryDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySubQueryDesigners
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QuerySubQueryDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuerySubQueryDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySubQueryDesigner item
   Description: Calls GetByID to retrieve the QuerySubQueryDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQueryDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company, QueryID, SubQueryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuerySubQueryDesigner for the service
   Description: Calls UpdateExt to update QuerySubQueryDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuerySubQueryDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company, QueryID, SubQueryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuerySubQueryDesigner item
   Description: Call UpdateExt to delete QuerySubQueryDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuerySubQueryDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryRelationDesigners(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryRelationDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelationDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelationDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company, QueryID, SubQueryID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelationDesigner item
   Description: Calls GetByID to retrieve the QueryRelationDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QuerySortByDesigners(Company, QueryID, SubQueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuerySortByDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySortByDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortByDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySortByDesigner item
   Description: Calls GetByID to retrieve the QuerySortByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortByDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryWhereItemDesigners(Company, QueryID, SubQueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryWhereItemDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryWhereItemDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItemDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company, QueryID, SubQueryID, TableID, CriteriaID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryWhereItemDesigner item
   Description: Calls GetByID to retrieve the QueryWhereItemDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItemDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param CriteriaID: Desc: CriteriaID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryGroupByDesigners(Company, QueryID, SubQueryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryGroupByDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryGroupByDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupByDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company, QueryID, SubQueryID, GroupByID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryGroupByDesigner item
   Description: Calls GetByID to retrieve the QueryGroupByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupByDesigner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param GroupByID: Desc: GroupByID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryTableDesigners(Company, QueryID, SubQueryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryTableDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryTableDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTableDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company, QueryID, SubQueryID, TableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryTableDesigner item
   Description: Calls GetByID to retrieve the QueryTableDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTableDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationDesigners(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryRelationDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelationDesigners
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryRelationDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryRelationDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company, QueryID, SubQueryID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelationDesigner item
   Description: Calls GetByID to retrieve the QueryRelationDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company, QueryID, SubQueryID, RelationID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryRelationDesigner for the service
   Description: Calls UpdateExt to update QueryRelationDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryRelationDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company, QueryID, SubQueryID, RelationID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryRelationDesigner item
   Description: Call UpdateExt to delete QueryRelationDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryRelationDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID_QueryRelationFieldDesigners(Company, QueryID, SubQueryID, RelationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryRelationFieldDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelationFieldDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFieldDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company, QueryID, SubQueryID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelationFieldDesigner item
   Description: Calls GetByID to retrieve the QueryRelationFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationFieldDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationFieldDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryRelationFieldDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelationFieldDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryRelationFieldDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryRelationFieldDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company, QueryID, SubQueryID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryRelationFieldDesigner item
   Description: Calls GetByID to retrieve the QueryRelationFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationFieldDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company, QueryID, SubQueryID, RelationID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryRelationFieldDesigner for the service
   Description: Calls UpdateExt to update QueryRelationFieldDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryRelationFieldDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company, QueryID, SubQueryID, RelationID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryRelationFieldDesigner item
   Description: Call UpdateExt to delete QueryRelationFieldDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryRelationFieldDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuerySortByDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuerySortByDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySortByDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QuerySortByDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuerySortByDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuerySortByDesigner item
   Description: Calls GetByID to retrieve the QuerySortByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortByDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuerySortByDesigner for the service
   Description: Calls UpdateExt to update QuerySortByDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuerySortByDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuerySortByDesigner item
   Description: Call UpdateExt to delete QuerySortByDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuerySortByDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryWhereItemDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryWhereItemDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryWhereItemDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryWhereItemDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryWhereItemDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company, QueryID, SubQueryID, TableID, CriteriaID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryWhereItemDesigner item
   Description: Calls GetByID to retrieve the QueryWhereItemDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItemDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param CriteriaID: Desc: CriteriaID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company, QueryID, SubQueryID, TableID, CriteriaID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryWhereItemDesigner for the service
   Description: Calls UpdateExt to update QueryWhereItemDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryWhereItemDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param CriteriaID: Desc: CriteriaID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company, QueryID, SubQueryID, TableID, CriteriaID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryWhereItemDesigner item
   Description: Call UpdateExt to delete QueryWhereItemDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryWhereItemDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param CriteriaID: Desc: CriteriaID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryGroupByDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryGroupByDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryGroupByDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryGroupByDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryGroupByDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company, QueryID, SubQueryID, GroupByID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryGroupByDesigner item
   Description: Calls GetByID to retrieve the QueryGroupByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupByDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param GroupByID: Desc: GroupByID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company, QueryID, SubQueryID, GroupByID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryGroupByDesigner for the service
   Description: Calls UpdateExt to update QueryGroupByDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryGroupByDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param GroupByID: Desc: GroupByID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company, QueryID, SubQueryID, GroupByID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryGroupByDesigner item
   Description: Call UpdateExt to delete QueryGroupByDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryGroupByDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param GroupByID: Desc: GroupByID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryTableDesigners(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryTableDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryTableDesigners
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryTableDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryTableDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company, QueryID, SubQueryID, TableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryTableDesigner item
   Description: Calls GetByID to retrieve the QueryTableDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTableDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company, QueryID, SubQueryID, TableID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryTableDesigner for the service
   Description: Calls UpdateExt to update QueryTableDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryTableDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company, QueryID, SubQueryID, TableID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryTableDesigner item
   Description: Call UpdateExt to delete QueryTableDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryTableDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFieldDesigners(Company, QueryID, SubQueryID, TableID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryFieldDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFieldDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFieldDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldDesigner item
   Description: Calls GetByID to retrieve the QueryFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFunctionCallDesigners(Company, QueryID, SubQueryID, TableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryFunctionCallDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFunctionCallDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCallDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company, QueryID, SubQueryID, TableID, FunctionID, ParameterName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFunctionCallDesigner item
   Description: Calls GetByID to retrieve the QueryFunctionCallDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCallDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldDesigners(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryFieldDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFieldDesigners
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryFieldDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryFieldDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldDesigner item
   Description: Calls GetByID to retrieve the QueryFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryFieldDesigner for the service
   Description: Calls UpdateExt to update QueryFieldDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryFieldDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company, QueryID, SubQueryID, TableID, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryFieldDesigner item
   Description: Call UpdateExt to delete QueryFieldDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryFieldDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributeDesigners(Company, QueryID, SubQueryID, TableID, FieldName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QueryFieldAttributeDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFieldAttributeDesigners1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributeDesigners",headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company, QueryID, SubQueryID, TableID, FieldName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldAttributeDesigner item
   Description: Calls GetByID to retrieve the QueryFieldAttributeDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttributeDesigner1
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldAttributeDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryFieldAttributeDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFieldAttributeDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryFieldAttributeDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryFieldAttributeDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company, QueryID, SubQueryID, TableID, FieldName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldAttributeDesigner item
   Description: Calls GetByID to retrieve the QueryFieldAttributeDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttributeDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company, QueryID, SubQueryID, TableID, FieldName, AttributeName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryFieldAttributeDesigner for the service
   Description: Calls UpdateExt to update QueryFieldAttributeDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryFieldAttributeDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company, QueryID, SubQueryID, TableID, FieldName, AttributeName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryFieldAttributeDesigner item
   Description: Call UpdateExt to delete QueryFieldAttributeDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryFieldAttributeDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFunctionCallDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryFunctionCallDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFunctionCallDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryFunctionCallDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryFunctionCallDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company, QueryID, SubQueryID, FunctionID, ParameterName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFunctionCallDesigner item
   Description: Calls GetByID to retrieve the QueryFunctionCallDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCallDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company, QueryID, SubQueryID, FunctionID, ParameterName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryFunctionCallDesigner for the service
   Description: Calls UpdateExt to update QueryFunctionCallDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryFunctionCallDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param FunctionID: Desc: FunctionID   Required: True   Allow empty value : True
      :param ParameterName: Desc: ParameterName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company, QueryID, SubQueryID, FunctionID, ParameterName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryFunctionCallDesigner item
   Description: Call UpdateExt to delete QueryFunctionCallDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryFunctionCallDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param SubQueryID: Desc: SubQueryID   Required: True   Allow empty value : True
      :param FunctionID: Desc: FunctionID   Required: True   Allow empty value : True
      :param ParameterName: Desc: ParameterName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateFieldDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateFieldDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateFieldDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryUpdateFieldDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryUpdateFieldDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company, QueryID, MapTableName, MapFieldName, Direction, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateFieldDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateFieldDesigner
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
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company, QueryID, MapTableName, MapFieldName, Direction, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryUpdateFieldDesigner for the service
   Description: Calls UpdateExt to update QueryUpdateFieldDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryUpdateFieldDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param MapTableName: Desc: MapTableName   Required: True   Allow empty value : True
      :param MapFieldName: Desc: MapFieldName   Required: True   Allow empty value : True
      :param Direction: Desc: Direction   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company, QueryID, MapTableName, MapFieldName, Direction, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryUpdateFieldDesigner item
   Description: Call UpdateExt to delete QueryUpdateFieldDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryUpdateFieldDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param MapTableName: Desc: MapTableName   Required: True   Allow empty value : True
      :param MapFieldName: Desc: MapFieldName   Required: True   Allow empty value : True
      :param Direction: Desc: Direction   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateSettingsDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateSettingsDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateSettingsDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryUpdateSettingsDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryUpdateSettingsDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryUpdateSettingsDesigners_Company_QueryID(Company, QueryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSettingsDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryUpdateSettingsDesigners_Company_QueryID(Company, QueryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryUpdateSettingsDesigner for the service
   Description: Calls UpdateExt to update QueryUpdateSettingsDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryUpdateSettingsDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryUpdateSettingsDesigners_Company_QueryID(Company, QueryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryUpdateSettingsDesigner item
   Description: Call UpdateExt to delete QueryUpdateSettingsDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryUpdateSettingsDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryValueSetItemsDesigners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QueryValueSetItemsDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryValueSetItemsDesigners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners",headers=creds) as resp:
           return await resp.json()

async def post_QueryValueSetItemsDesigners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryValueSetItemsDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company, QueryID, ValueSetID, ItemValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryValueSetItemsDesigner item
   Description: Calls GetByID to retrieve the QueryValueSetItemsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItemsDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ValueSetID: Desc: ValueSetID   Required: True   Allow empty value : True
      :param ItemValue: Desc: ItemValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company, QueryID, ValueSetID, ItemValue, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QueryValueSetItemsDesigner for the service
   Description: Calls UpdateExt to update QueryValueSetItemsDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryValueSetItemsDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ValueSetID: Desc: ValueSetID   Required: True   Allow empty value : True
      :param ItemValue: Desc: ItemValue   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company, QueryID, ValueSetID, ItemValue, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QueryValueSetItemsDesigner item
   Description: Call UpdateExt to delete QueryValueSetItemsDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryValueSetItemsDesigner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param ValueSetID: Desc: ValueSetID   Required: True   Allow empty value : True
      :param ItemValue: Desc: ItemValue   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DynamicQueryDesignerListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynamicQueryDesigner, whereClauseQueryCtrlDesigner, whereClauseQueryCtrlValuesDesigner, whereClauseQueryCustomActionDesigner, whereClauseQueryExecuteSettingDesigner, whereClauseQueryParameterDesigner, whereClauseQueryReferenceDesigner, whereClauseQueryParameterBindingDesigner, whereClauseQuerySubQueryDesigner, whereClauseQueryRelationDesigner, whereClauseQueryRelationFieldDesigner, whereClauseQuerySortByDesigner, whereClauseQueryWhereItemDesigner, whereClauseQueryGroupByDesigner, whereClauseQueryTableDesigner, whereClauseQueryFieldDesigner, whereClauseQueryFieldAttributeDesigner, whereClauseQueryFunctionCallDesigner, whereClauseQueryUpdateFieldDesigner, whereClauseQueryUpdateSettingsDesigner, whereClauseQueryValueSetItemsDesigner, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
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
   params += "whereClauseDynamicQueryDesigner=" + whereClauseDynamicQueryDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryCtrlDesigner=" + whereClauseQueryCtrlDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryCtrlValuesDesigner=" + whereClauseQueryCtrlValuesDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryCustomActionDesigner=" + whereClauseQueryCustomActionDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryExecuteSettingDesigner=" + whereClauseQueryExecuteSettingDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryParameterDesigner=" + whereClauseQueryParameterDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryReferenceDesigner=" + whereClauseQueryReferenceDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryParameterBindingDesigner=" + whereClauseQueryParameterBindingDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuerySubQueryDesigner=" + whereClauseQuerySubQueryDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryRelationDesigner=" + whereClauseQueryRelationDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryRelationFieldDesigner=" + whereClauseQueryRelationFieldDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuerySortByDesigner=" + whereClauseQuerySortByDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryWhereItemDesigner=" + whereClauseQueryWhereItemDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryGroupByDesigner=" + whereClauseQueryGroupByDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryTableDesigner=" + whereClauseQueryTableDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryFieldDesigner=" + whereClauseQueryFieldDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryFieldAttributeDesigner=" + whereClauseQueryFieldAttributeDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryFunctionCallDesigner=" + whereClauseQueryFunctionCallDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryUpdateFieldDesigner=" + whereClauseQueryUpdateFieldDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryUpdateSettingsDesigner=" + whereClauseQueryUpdateSettingsDesigner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQueryValueSetItemsDesigner=" + whereClauseQueryValueSetItemsDesigner
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(queryID, epicorHeaders = None):
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
   params += "queryID=" + queryID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDEx
   Description: GetByID with Mode parameters
   OperationID: GetByIDEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportQuery(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportQuery
   Description: Commits the DataSet changes to the data store by skipping rules.
   OperationID: ImportQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByCompanyAndID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByCompanyAndID
   Description: delete specified query from specified company
   OperationID: DeleteByCompanyAndID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByCompanyAndID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByCompanyAndID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUsedInBAQList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUsedInBAQList
   Description: Get lists  where specified query is used
   OperationID: GetUsedInBAQList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUsedInBAQList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsedInBAQList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTableList(epicorHeaders = None):
   """  
   Summary: Invoke method GetTableList
   Description: Get full list of tables from zDataTable for palette and code editor
   OperationID: GetTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldList
   Description: select physical columns info from db and z-tables
   OperationID: GetFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBAQColumnList(queryID, epicorHeaders = None):
   """  
   Summary: Invoke method GetBAQColumnList
   Description: Get BAQ columns list
   OperationID: Get_GetBAQColumnList
      :param queryID: Desc: BAQ identifier   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "queryID=" + queryID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetFirstBAQColumn(queryID, epicorHeaders = None):
   """  
   Summary: Invoke method GetFirstBAQColumn
   Description: Get first BAQ column
   OperationID: Get_GetFirstBAQColumn
      :param queryID: Desc: BAQ identifier   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFirstBAQColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "queryID=" + queryID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetZTableInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetZTableInfo
   Description: Get table information(description) from z-data
   OperationID: GetZTableInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetZTableInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetZTableInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDBTableNameByTableID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDBTableNameByTableID
   Description: Get table database name from z-data
   OperationID: GetDBTableNameByTableID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDBTableNameByTableID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBTableNameByTableID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBOTableFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBOTableFieldList
   Description: Select BO table info from z-tables
   OperationID: GetBOTableFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOTableFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOTableFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExecutionSettings(epicorHeaders = None):
   """  
   Summary: Invoke method GetExecutionSettings
   Description: Execution settings supported by the dynamic query
   OperationID: GetExecutionSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExecutionSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSvcList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSvcList
   OperationID: GetSvcList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSvcList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_LoadQueryDiagram(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadQueryDiagram
   Description: This method returns serialized query diagram for classic BAQ Designer.
   OperationID: LoadQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadKineticQueryDiagram(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadKineticQueryDiagram
   Description: This method returns serialized query diagram for Kinetic BAQ Designer.
   OperationID: LoadKineticQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadKineticQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadKineticQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteQueryDiagram(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteQueryDiagram
   Description: This method deletes query diagram both for classic and kinetic version.
   OperationID: DeleteQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveQueryDiagram(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveQueryDiagram
   Description: This method saves SOAP-serialized query diagram
   OperationID: SaveQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateQueryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateQueryID
   Description: Check if query name entered is valid
   OperationID: ValidateQueryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQueryCompanyLists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQueryCompanyLists
   Description: Check if company can be made global - no such query ids in other companies
   OperationID: GetQueryCompanyLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryCompanyLists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryCompanyLists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AvailableCGCCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AvailableCGCCodes
   Description: Country codes available for company
   OperationID: AvailableCGCCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AvailableCGCCodes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AvailableCGCCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PossibleBONames(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PossibleBONames
   Description: returns list of BOs where query tables are used
   OperationID: PossibleBONames
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PossibleBONames_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PossibleBONames_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBOTableList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBOTableList
   Description: This method returns the list of tables, belonging to specified business object
   OperationID: GetBOTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateQuerySecurityFilters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateQuerySecurityFilters
   Description: Updates security filters for provided query
   OperationID: UpdateQuerySecurityFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateQuerySecurityFilters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateQuerySecurityFilters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateQueriesSecurityFiltersByDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateQueriesSecurityFiltersByDs
   Description: Iterates through each query refers to specified External Datasource or to any of External Datasources linked to specified External Datasource types
and updates security filters
   OperationID: UpdateQueriesSecurityFiltersByDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateQueriesSecurityFiltersByDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateQueriesSecurityFiltersByDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegenUpdatableQueryBpm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RegenUpdatableQueryBpm
   Description: Regenerate Updatable Query Bpm code
   OperationID: RegenUpdatableQueryBpm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenUpdatableQueryBpm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenUpdatableQueryBpm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillDisplayFieldAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillDisplayFieldAttributes
   Description: Fills attributes for display fields in query if field properties like FieldLabel differ from system settings.
Method is used by query import and BAQUpgrade routine
   OperationID: FillDisplayFieldAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillDisplayFieldAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillDisplayFieldAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateASP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateASP
   Description: Generate Asp file
   OperationID: GenerateASP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateASP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateASP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetASPFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetASPFields
   Description: Get  Fields list for Asp
   OperationID: GetASPFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetASPFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetASPFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSecurityCodeForCurrentCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSecurityCodeForCurrentCompany
   Description: Check query security code for the current company
   OperationID: CheckSecurityCodeForCurrentCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSecurityCodeForCurrentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSecurityCodeForCurrentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTableExtensions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTableExtensions
   Description: Return extension tables for table schemaName.dbTableName
   OperationID: GetTableExtensions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableExtensions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableExtensions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetSecurityCodeToSystemQuery(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSecurityCodeToSystemQuery
   Description: Overrides security code assigned to system query with passed security code.
System query should exists. If ordinal query found by specified id or nothing found then exception is raised.
Security code should exists. If security code is not found then exception is raised.
   OperationID: SetSecurityCodeToSystemQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSecurityCodeToSystemQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSecurityCodeToSystemQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultSecurityCodeOfSystemQuery(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultSecurityCodeOfSystemQuery
   Description: Get default security code assigned to system query with passed security code.
System query should exists. If ordinal query found by specified id or nothing found then exception is raised.
   OperationID: GetDefaultSecurityCodeOfSystemQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultSecurityCodeOfSystemQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultSecurityCodeOfSystemQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetCache(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetCache
   Description: Reset specified server-side caches related to BAQ engine
   OperationID: ResetCache
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetCache_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportBaq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportBaq
   OperationID: ExportBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBAQDataSetByContent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBAQDataSetByContent
   Description: Get BAQ Designer DataSet by content (array of bytes).
   OperationID: GetBAQDataSetByContent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBAQDataSetByContent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQDataSetByContent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportBaq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportBaq
   OperationID: ImportBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynamicQueryDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynamicQueryDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynamicQueryDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynamicQueryDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynamicQueryDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryCtrlDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryCtrlDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryCtrlDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryCtrlDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryCtrlDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryCtrlValuesDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryCtrlValuesDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryCtrlValuesDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryCtrlValuesDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryCtrlValuesDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryCustomActionDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryCustomActionDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryCustomActionDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryCustomActionDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryCustomActionDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryExecuteSettingDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryExecuteSettingDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryExecuteSettingDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryExecuteSettingDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryExecuteSettingDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryParameterDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryParameterDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryParameterDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryParameterDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryParameterDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryReferenceDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryReferenceDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryReferenceDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryReferenceDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryReferenceDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryParameterBindingDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryParameterBindingDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryParameterBindingDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryParameterBindingDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryParameterBindingDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuerySubQueryDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuerySubQueryDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuerySubQueryDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuerySubQueryDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuerySubQueryDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryRelationDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryRelationDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryRelationDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryRelationDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryRelationDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryRelationFieldDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryRelationFieldDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryRelationFieldDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryRelationFieldDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryRelationFieldDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuerySortByDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuerySortByDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuerySortByDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuerySortByDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuerySortByDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryWhereItemDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryWhereItemDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryWhereItemDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryWhereItemDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryWhereItemDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryGroupByDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryGroupByDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryGroupByDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryGroupByDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryGroupByDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryTableDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryTableDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryTableDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryTableDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryTableDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryFieldDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryFieldDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryFieldDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryFieldDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryFieldDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryFieldAttributeDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryFieldAttributeDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryFieldAttributeDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryFieldAttributeDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryFieldAttributeDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryFunctionCallDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryFunctionCallDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryFunctionCallDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryFunctionCallDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryFunctionCallDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryUpdateFieldDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryUpdateFieldDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryUpdateFieldDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryUpdateFieldDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryUpdateFieldDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryUpdateSettingsDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryUpdateSettingsDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryUpdateSettingsDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryUpdateSettingsDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryUpdateSettingsDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQueryValueSetItemsDesigner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQueryValueSetItemsDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryValueSetItemsDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryValueSetItemsDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryValueSetItemsDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupUserList(epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupUserList
   Description: This method returns an string with the group access list by user.
   OperationID: GetGroupUserList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DynamicQueryDesignerListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DynamicQueryDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryCtrlDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryCtrlValuesDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryCustomActionDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryExecuteSettingDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryFieldAttributeDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryFieldDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryFunctionCallDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryGroupByDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryParameterBindingDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryParameterDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryReferenceDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryRelationDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryRelationFieldDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuerySortByDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuerySubQueryDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryTableDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryUpdateFieldDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryUpdateSettingsDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryValueSetItemsDesignerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemDesignerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryWhereItemDesignerRow] = obj["value"]
      pass

class Ice_Tablesets_DynamicQueryDesignerListRow:
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
      self.UseLiveDB:bool = obj["UseLiveDB"]
      """  UseLiveDB  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DynamicQueryDesignerRow:
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
      self.UseLiveDB:bool = obj["UseLiveDB"]
      """  UseLiveDB  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.BPMUpdateOnly:bool = obj["BPMUpdateOnly"]
      """  true if update through BO is not used  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryCtrlDesignerRow:
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

class Ice_Tablesets_QueryCtrlValuesDesignerRow:
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

class Ice_Tablesets_QueryCustomActionDesignerRow:
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

class Ice_Tablesets_QueryExecuteSettingDesignerRow:
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

class Ice_Tablesets_QueryFieldAttributeDesignerRow:
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
      """  Flags whether the attribute was changed by user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFieldDesignerRow:
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
      self.IsRequired:bool = obj["IsRequired"]
      """  IsRequired  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  IsReadOnly  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SubquerySet_Alias:str = obj["SubquerySet_Alias"]
      self.SubquerySet_DataType:str = obj["SubquerySet_DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFunctionCallDesignerRow:
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

class Ice_Tablesets_QueryGroupByDesignerRow:
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

class Ice_Tablesets_QueryParameterBindingDesignerRow:
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

class Ice_Tablesets_QueryParameterDesignerRow:
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

class Ice_Tablesets_QueryReferenceDesignerRow:
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

class Ice_Tablesets_QueryRelationDesignerRow:
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

class Ice_Tablesets_QueryRelationFieldDesignerRow:
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

class Ice_Tablesets_QuerySortByDesignerRow:
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

class Ice_Tablesets_QuerySubQueryDesignerRow:
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

class Ice_Tablesets_QueryTableDesignerRow:
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

class Ice_Tablesets_QueryUpdateFieldDesignerRow:
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
      self.Description:str = obj["Description"]
      """  Shows field description - taken from zDataField  """  
      self.QualifiedName:str = obj["QualifiedName"]
      """  DBTableName + "." + DBFieldName  """  
      self.Required:bool = obj["Required"]
      """  Shows if field is required - taken from zDataField  """  
      self.DataType:str = obj["DataType"]
      """  Shows field data type - taken from zDataField  """  
      self.NullableType:bool = obj["NullableType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryUpdateSettingsDesignerRow:
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

class Ice_Tablesets_QueryValueSetItemsDesignerRow:
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

class Ice_Tablesets_QueryWhereItemDesignerRow:
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
      self.UseHaving:bool = obj["UseHaving"]
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
class AvailableCGCCodes_input:
   """ Required : 
   crossCompany
   """  
   def __init__(self, obj):
      self.crossCompany:bool = obj["crossCompany"]
      pass

class AvailableCGCCodes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class CheckSecurityCodeForCurrentCompany_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      pass

class CheckSecurityCodeForCurrentCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isSecCodeExists:bool = obj["isSecCodeExists"]
      self.isSecCodeAvailable:bool = obj["isSecCodeAvailable"]
      pass

      """  output parameters  """  

class DeleteByCompanyAndID_input:
   """ Required : 
   company
   queryID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company ID  """  
      self.queryID:str = obj["queryID"]
      """  Query ID  """  
      pass

class DeleteByCompanyAndID_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteQueryDiagram_input:
   """ Required : 
   queryID
   companyID
   userID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query(QueryHdr) ID  """  
      self.companyID:str = obj["companyID"]
      """  The Company) ID  """  
      self.userID:str = obj["userID"]
      """  The User ID  """  
      pass

class DeleteQueryDiagram_output:
   def __init__(self, obj):
      pass

class ExportBaq_input:
   """ Required : 
   queryId
   options
   """  
   def __init__(self, obj):
      self.queryId:str = obj["queryId"]
      self.options      #schema had no properties on an object.
      pass

class ExportBaq_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.options: UNKNOW TYPE(error 2338) = obj["options"]
      self.logResult:list = obj[any]
      pass

      """  output parameters  """  

class FillDisplayFieldAttributes_input:
   """ Required : 
   companyID
   queryID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.queryID:str = obj["queryID"]
      pass

class FillDisplayFieldAttributes_output:
   def __init__(self, obj):
      pass

class GenerateASP_input:
   """ Required : 
   pcQueryID
   pcFilename
   ds
   """  
   def __init__(self, obj):
      self.pcQueryID:str = obj["pcQueryID"]
      self.pcFilename:str = obj["pcFilename"]
      self.ds:list[Ice_Tablesets_AspExportFieldTableset] = obj["ds"]
      pass

class GenerateASP_output:
   def __init__(self, obj):
      pass

class GetASPFields_input:
   """ Required : 
   pcQueryID
   """  
   def __init__(self, obj):
      self.pcQueryID:str = obj["pcQueryID"]
      pass

class GetASPFields_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AspExportFieldTableset] = obj["returnObj"]
      pass

class GetBAQColumnList_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  BAQ identifier  """  
      pass

class GetBAQColumnList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetBAQDataSetByContent_input:
   """ Required : 
   contentBytes
   """  
   def __init__(self, obj):
      self.contentBytes:str = obj["contentBytes"]
      """  Content.  """  
      pass

class GetBAQDataSetByContent_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetBOTableFieldList_input:
   """ Required : 
   dataTableID
   schema
   """  
   def __init__(self, obj):
      self.dataTableID:str = obj["dataTableID"]
      self.schema:str = obj["schema"]
      pass

class GetBOTableFieldList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TableFieldListTableset] = obj["returnObj"]
      pass

class GetBOTableList_input:
   """ Required : 
   boName
   """  
   def __init__(self, obj):
      self.boName:str = obj["boName"]
      """  Business Object Name in form SystemCode.BOName  """  
      pass

class GetBOTableList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQBOTablesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.topTableID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByIDEx_input:
   """ Required : 
   queryID
   mode
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      self.mode:int = obj["mode"]
      pass

class GetByIDEx_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQDesignerTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQDesignerTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQDesignerTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQDesignerTableset] = obj["returnObj"]
      pass

class GetDBTableNameByTableID_input:
   """ Required : 
   dataTableID
   systemCode
   """  
   def __init__(self, obj):
      self.dataTableID:str = obj["dataTableID"]
      """  DataTableID  """  
      self.systemCode:str = obj["systemCode"]
      """  DB schema (systemCode)  """  
      pass

class GetDBTableNameByTableID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if this information found  """  
      pass

   def parameters(self, obj):
      self.dbTableName:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultSecurityCodeOfSystemQuery_input:
   """ Required : 
   queryId
   """  
   def __init__(self, obj):
      self.queryId:str = obj["queryId"]
      """  Id of system query  """  
      pass

class GetDefaultSecurityCodeOfSystemQuery_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Default security code  """  
      pass

class GetExecutionSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExecSettingListTableset] = obj["returnObj"]
      pass

class GetFieldList_input:
   """ Required : 
   dataTableID
   schema
   """  
   def __init__(self, obj):
      self.dataTableID:str = obj["dataTableID"]
      self.schema:str = obj["schema"]
      pass

class GetFieldList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TableFieldListTableset] = obj["returnObj"]
      pass

class GetFirstBAQColumn_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  BAQ identifier  """  
      pass

class GetFirstBAQColumn_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetGroupUserList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.groupUserList:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Ice_Tablesets_BAQDesignerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDynamicQueryDesigner_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

class GetNewDynamicQueryDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryCtrlDesigner_input:
   """ Required : 
   ds
   queryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      pass

class GetNewQueryCtrlDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryCtrlValuesDesigner_input:
   """ Required : 
   ds
   queryID
   controlID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.controlID:str = obj["controlID"]
      pass

class GetNewQueryCtrlValuesDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryCustomActionDesigner_input:
   """ Required : 
   ds
   queryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      pass

class GetNewQueryCustomActionDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryExecuteSettingDesigner_input:
   """ Required : 
   ds
   queryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      pass

class GetNewQueryExecuteSettingDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryFieldAttributeDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   tableID
   fieldName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      self.tableID:str = obj["tableID"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetNewQueryFieldAttributeDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryFieldDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   tableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      self.tableID:str = obj["tableID"]
      pass

class GetNewQueryFieldDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryFunctionCallDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   functionID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      self.functionID:str = obj["functionID"]
      pass

class GetNewQueryFunctionCallDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryGroupByDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      pass

class GetNewQueryGroupByDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryParameterBindingDesigner_input:
   """ Required : 
   ds
   queryID
   referenceID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.referenceID:str = obj["referenceID"]
      pass

class GetNewQueryParameterBindingDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryParameterDesigner_input:
   """ Required : 
   ds
   queryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      pass

class GetNewQueryParameterDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryReferenceDesigner_input:
   """ Required : 
   ds
   queryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      pass

class GetNewQueryReferenceDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryRelationDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      pass

class GetNewQueryRelationDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryRelationFieldDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   relationID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      self.relationID:str = obj["relationID"]
      pass

class GetNewQueryRelationFieldDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuerySortByDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   tableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      self.tableID:str = obj["tableID"]
      pass

class GetNewQuerySortByDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuerySubQueryDesigner_input:
   """ Required : 
   ds
   queryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      pass

class GetNewQuerySubQueryDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryTableDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      pass

class GetNewQueryTableDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryUpdateFieldDesigner_input:
   """ Required : 
   ds
   queryID
   mapTableName
   mapFieldName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.mapTableName:str = obj["mapTableName"]
      self.mapFieldName:str = obj["mapFieldName"]
      pass

class GetNewQueryUpdateFieldDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryUpdateSettingsDesigner_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

class GetNewQueryUpdateSettingsDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryValueSetItemsDesigner_input:
   """ Required : 
   ds
   queryID
   valueSetID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.valueSetID:str = obj["valueSetID"]
      pass

class GetNewQueryValueSetItemsDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQueryWhereItemDesigner_input:
   """ Required : 
   ds
   queryID
   subQueryID
   tableID
   criteriaID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      self.subQueryID:str = obj["subQueryID"]
      self.tableID:str = obj["tableID"]
      self.criteriaID:str = obj["criteriaID"]
      pass

class GetNewQueryWhereItemDesigner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetQueryCompanyLists_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  query id to check  """  
      pass

class GetQueryCompanyLists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.globalInCompany:str = obj["parameters"]
      self.localInCompanies:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDynamicQueryDesigner
   whereClauseQueryCtrlDesigner
   whereClauseQueryCtrlValuesDesigner
   whereClauseQueryCustomActionDesigner
   whereClauseQueryExecuteSettingDesigner
   whereClauseQueryParameterDesigner
   whereClauseQueryReferenceDesigner
   whereClauseQueryParameterBindingDesigner
   whereClauseQuerySubQueryDesigner
   whereClauseQueryRelationDesigner
   whereClauseQueryRelationFieldDesigner
   whereClauseQuerySortByDesigner
   whereClauseQueryWhereItemDesigner
   whereClauseQueryGroupByDesigner
   whereClauseQueryTableDesigner
   whereClauseQueryFieldDesigner
   whereClauseQueryFieldAttributeDesigner
   whereClauseQueryFunctionCallDesigner
   whereClauseQueryUpdateFieldDesigner
   whereClauseQueryUpdateSettingsDesigner
   whereClauseQueryValueSetItemsDesigner
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynamicQueryDesigner:str = obj["whereClauseDynamicQueryDesigner"]
      self.whereClauseQueryCtrlDesigner:str = obj["whereClauseQueryCtrlDesigner"]
      self.whereClauseQueryCtrlValuesDesigner:str = obj["whereClauseQueryCtrlValuesDesigner"]
      self.whereClauseQueryCustomActionDesigner:str = obj["whereClauseQueryCustomActionDesigner"]
      self.whereClauseQueryExecuteSettingDesigner:str = obj["whereClauseQueryExecuteSettingDesigner"]
      self.whereClauseQueryParameterDesigner:str = obj["whereClauseQueryParameterDesigner"]
      self.whereClauseQueryReferenceDesigner:str = obj["whereClauseQueryReferenceDesigner"]
      self.whereClauseQueryParameterBindingDesigner:str = obj["whereClauseQueryParameterBindingDesigner"]
      self.whereClauseQuerySubQueryDesigner:str = obj["whereClauseQuerySubQueryDesigner"]
      self.whereClauseQueryRelationDesigner:str = obj["whereClauseQueryRelationDesigner"]
      self.whereClauseQueryRelationFieldDesigner:str = obj["whereClauseQueryRelationFieldDesigner"]
      self.whereClauseQuerySortByDesigner:str = obj["whereClauseQuerySortByDesigner"]
      self.whereClauseQueryWhereItemDesigner:str = obj["whereClauseQueryWhereItemDesigner"]
      self.whereClauseQueryGroupByDesigner:str = obj["whereClauseQueryGroupByDesigner"]
      self.whereClauseQueryTableDesigner:str = obj["whereClauseQueryTableDesigner"]
      self.whereClauseQueryFieldDesigner:str = obj["whereClauseQueryFieldDesigner"]
      self.whereClauseQueryFieldAttributeDesigner:str = obj["whereClauseQueryFieldAttributeDesigner"]
      self.whereClauseQueryFunctionCallDesigner:str = obj["whereClauseQueryFunctionCallDesigner"]
      self.whereClauseQueryUpdateFieldDesigner:str = obj["whereClauseQueryUpdateFieldDesigner"]
      self.whereClauseQueryUpdateSettingsDesigner:str = obj["whereClauseQueryUpdateSettingsDesigner"]
      self.whereClauseQueryValueSetItemsDesigner:str = obj["whereClauseQueryValueSetItemsDesigner"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQDesignerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSvcList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SvcListTableset] = obj["returnObj"]
      pass

class GetTableExtensions_input:
   """ Required : 
   schemaName
   dbTableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Extended table schema  """  
      self.dbTableName:str = obj["dbTableName"]
      """  Extended table db name  """  
      pass

class GetTableExtensions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_ExtendedTableInfo] = obj["returnObj"]
      pass

class GetTableList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FullTableListTableset] = obj["returnObj"]
      pass

class GetUsedInBAQList_input:
   """ Required : 
   queryID
   isGlobalQuery
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query(Exports) ID  """  
      self.isGlobalQuery:bool = obj["isGlobalQuery"]
      """  isGlobalQuery  """  
      pass

class GetUsedInBAQList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UsedInBAQListTableset] = obj["returnObj"]
      pass

class GetZTableInfo_input:
   """ Required : 
   dbTableName
   schema
   """  
   def __init__(self, obj):
      self.dbTableName:str = obj["dbTableName"]
      """  DB Table Name  """  
      self.schema:str = obj["schema"]
      """  DB schema (systemCode)  """  
      pass

class GetZTableInfo_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if this information found  """  
      pass

   def parameters(self, obj):
      self.description:str = obj["parameters"]
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

class Ice_Contracts_ExtendedTableInfo:
   def __init__(self, obj):
      self.SchemaName:str = obj["SchemaName"]
      self.DBTableName:str = obj["DBTableName"]
      self.ExtensionTables:list[Ice_Contracts_ExtensionTableInfo] = obj["ExtensionTables"]
      pass

class Ice_Contracts_ExtensionTableInfo:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.SchemaName:str = obj["SchemaName"]
      self.DBTableName:str = obj["DBTableName"]
      self.TableType:str = obj["TableType"]
      self.Relations:list[Ice_Contracts_ExtensionTableRelationInfo] = obj["Relations"]
      pass

class Ice_Contracts_ExtensionTableRelationColumnInfo:
   def __init__(self, obj):
      self.ExtendedTableColumn:str = obj["ExtendedTableColumn"]
      self.ExtensionTableColumn:str = obj["ExtensionTableColumn"]
      self.CompOp:str = obj["CompOp"]
      pass

class Ice_Contracts_ExtensionTableRelationInfo:
   def __init__(self, obj):
      self.RelationID:str = obj["RelationID"]
      self.ExtensionSchemaName:str = obj["ExtensionSchemaName"]
      self.ExtensionTableName:str = obj["ExtensionTableName"]
      self.Join:int = obj["Join"]
      self.Columns:list[Ice_Contracts_ExtensionTableRelationColumnInfo] = obj["Columns"]
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

class Ice_Tablesets_AspExportFieldRow:
   def __init__(self, obj):
      self.QueryID:str = obj["QueryID"]
      self.Seq:int = obj["Seq"]
      self.FieldName:str = obj["FieldName"]
      self.Description:str = obj["Description"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.FieldOrder:int = obj["FieldOrder"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FieldSearch:str = obj["FieldSearch"]
      self.SearchOptions:str = obj["SearchOptions"]
      self.ShowField:bool = obj["ShowField"]
      self.SearchField:bool = obj["SearchField"]
      self.IsNumeric:bool = obj["IsNumeric"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AspExportFieldTableset:
   def __init__(self, obj):
      self.AspExportField:list[Ice_Tablesets_AspExportFieldRow] = obj["AspExportField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQBOTablesTableset:
   def __init__(self, obj):
      self.BAQBOtables:list[Ice_Tablesets_BAQBOtablesRow] = obj["BAQBOtables"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQBOtablesRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.ParentTableID:str = obj["ParentTableID"]
      self.TableType:str = obj["TableType"]
      self.SystemCode:str = obj["SystemCode"]
      self.DBTableName:str = obj["DBTableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQDesignerListTableset:
   def __init__(self, obj):
      self.DynamicQueryDesignerList:list[Ice_Tablesets_DynamicQueryDesignerListRow] = obj["DynamicQueryDesignerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQDesignerTableset:
   def __init__(self, obj):
      self.DynamicQueryDesigner:list[Ice_Tablesets_DynamicQueryDesignerRow] = obj["DynamicQueryDesigner"]
      self.QueryCtrlDesigner:list[Ice_Tablesets_QueryCtrlDesignerRow] = obj["QueryCtrlDesigner"]
      self.QueryCtrlValuesDesigner:list[Ice_Tablesets_QueryCtrlValuesDesignerRow] = obj["QueryCtrlValuesDesigner"]
      self.QueryCustomActionDesigner:list[Ice_Tablesets_QueryCustomActionDesignerRow] = obj["QueryCustomActionDesigner"]
      self.QueryExecuteSettingDesigner:list[Ice_Tablesets_QueryExecuteSettingDesignerRow] = obj["QueryExecuteSettingDesigner"]
      self.QueryParameterDesigner:list[Ice_Tablesets_QueryParameterDesignerRow] = obj["QueryParameterDesigner"]
      self.QueryReferenceDesigner:list[Ice_Tablesets_QueryReferenceDesignerRow] = obj["QueryReferenceDesigner"]
      self.QueryParameterBindingDesigner:list[Ice_Tablesets_QueryParameterBindingDesignerRow] = obj["QueryParameterBindingDesigner"]
      self.QuerySubQueryDesigner:list[Ice_Tablesets_QuerySubQueryDesignerRow] = obj["QuerySubQueryDesigner"]
      self.QueryRelationDesigner:list[Ice_Tablesets_QueryRelationDesignerRow] = obj["QueryRelationDesigner"]
      self.QueryRelationFieldDesigner:list[Ice_Tablesets_QueryRelationFieldDesignerRow] = obj["QueryRelationFieldDesigner"]
      self.QuerySortByDesigner:list[Ice_Tablesets_QuerySortByDesignerRow] = obj["QuerySortByDesigner"]
      self.QueryWhereItemDesigner:list[Ice_Tablesets_QueryWhereItemDesignerRow] = obj["QueryWhereItemDesigner"]
      self.QueryGroupByDesigner:list[Ice_Tablesets_QueryGroupByDesignerRow] = obj["QueryGroupByDesigner"]
      self.QueryTableDesigner:list[Ice_Tablesets_QueryTableDesignerRow] = obj["QueryTableDesigner"]
      self.QueryFieldDesigner:list[Ice_Tablesets_QueryFieldDesignerRow] = obj["QueryFieldDesigner"]
      self.QueryFieldAttributeDesigner:list[Ice_Tablesets_QueryFieldAttributeDesignerRow] = obj["QueryFieldAttributeDesigner"]
      self.QueryFunctionCallDesigner:list[Ice_Tablesets_QueryFunctionCallDesignerRow] = obj["QueryFunctionCallDesigner"]
      self.QueryUpdateFieldDesigner:list[Ice_Tablesets_QueryUpdateFieldDesignerRow] = obj["QueryUpdateFieldDesigner"]
      self.QueryUpdateSettingsDesigner:list[Ice_Tablesets_QueryUpdateSettingsDesignerRow] = obj["QueryUpdateSettingsDesigner"]
      self.QueryValueSetItemsDesigner:list[Ice_Tablesets_QueryValueSetItemsDesignerRow] = obj["QueryValueSetItemsDesigner"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title for this report  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates the report is a system deliver report.  """  
      self.GlobalReport:bool = obj["GlobalReport"]
      """  true if this report is available to all companies  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.QueryID:str = obj["QueryID"]
      """  Query ID  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DynamicQueryDesignerListRow:
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
      self.UseLiveDB:bool = obj["UseLiveDB"]
      """  UseLiveDB  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DynamicQueryDesignerRow:
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
      self.UseLiveDB:bool = obj["UseLiveDB"]
      """  UseLiveDB  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.BPMUpdateOnly:bool = obj["BPMUpdateOnly"]
      """  true if update through BO is not used  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExecSettingListRow:
   def __init__(self, obj):
      self.SettingID:str = obj["SettingID"]
      self.SettingType:str = obj["SettingType"]
      self.DefaultValue:str = obj["DefaultValue"]
      self.Required:bool = obj["Required"]
      self.IsEnum:bool = obj["IsEnum"]
      self.Description:str = obj["Description"]
      self.Category:str = obj["Category"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExecSettingListTableset:
   def __init__(self, obj):
      self.ExecSettingList:list[Ice_Tablesets_ExecSettingListRow] = obj["ExecSettingList"]
      self.ExecSettingValues:list[Ice_Tablesets_ExecSettingValuesRow] = obj["ExecSettingValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExecSettingValuesRow:
   def __init__(self, obj):
      self.SettingID:str = obj["SettingID"]
      self.SettingEnumValue:str = obj["SettingEnumValue"]
      self.SettingValueOrder:int = obj["SettingValueOrder"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_FullTableListRow:
   def __init__(self, obj):
      self.TableID:str = obj["TableID"]
      """  DataTableID from zDataTable  """  
      self.Description:str = obj["Description"]
      """  Description from zDataTable  """  
      self.TableType:str = obj["TableType"]
      """  DB = Database, TT = Temp Table from ZDataTable  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  Db Schema of the Database table from Ice.Table view  """  
      self.FullTableName:str = obj["FullTableName"]
      """  Db Schema of the Database table  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_FullTableListTableset:
   def __init__(self, obj):
      self.FullTableList:list[Ice_Tablesets_FullTableListRow] = obj["FullTableList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QueryCtrlDesignerRow:
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

class Ice_Tablesets_QueryCtrlValuesDesignerRow:
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

class Ice_Tablesets_QueryCustomActionDesignerRow:
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

class Ice_Tablesets_QueryDiagramRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.Data:str = obj["Data"]
      """  Data  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsKinetic:bool = obj["IsKinetic"]
      """  IsKinetic  """  
      self.DiagramVersion:str = obj["DiagramVersion"]
      """  DiagramVersion  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryDiagramTableset:
   def __init__(self, obj):
      self.QueryDiagram:list[Ice_Tablesets_QueryDiagramRow] = obj["QueryDiagram"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QueryExecuteSettingDesignerRow:
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

class Ice_Tablesets_QueryFieldAttributeDesignerRow:
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
      """  Flags whether the attribute was changed by user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFieldDesignerRow:
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
      self.IsRequired:bool = obj["IsRequired"]
      """  IsRequired  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  IsReadOnly  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SubquerySet_Alias:str = obj["SubquerySet_Alias"]
      self.SubquerySet_DataType:str = obj["SubquerySet_DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFunctionCallDesignerRow:
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

class Ice_Tablesets_QueryGroupByDesignerRow:
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

class Ice_Tablesets_QueryParameterBindingDesignerRow:
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

class Ice_Tablesets_QueryParameterDesignerRow:
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

class Ice_Tablesets_QueryReferenceDesignerRow:
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

class Ice_Tablesets_QueryRelationDesignerRow:
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

class Ice_Tablesets_QueryRelationFieldDesignerRow:
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

class Ice_Tablesets_QuerySortByDesignerRow:
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

class Ice_Tablesets_QuerySubQueryDesignerRow:
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

class Ice_Tablesets_QueryTableDesignerRow:
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

class Ice_Tablesets_QueryUpdateFieldDesignerRow:
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
      self.Description:str = obj["Description"]
      """  Shows field description - taken from zDataField  """  
      self.QualifiedName:str = obj["QualifiedName"]
      """  DBTableName + "." + DBFieldName  """  
      self.Required:bool = obj["Required"]
      """  Shows if field is required - taken from zDataField  """  
      self.DataType:str = obj["DataType"]
      """  Shows field data type - taken from zDataField  """  
      self.NullableType:bool = obj["NullableType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryUpdateSettingsDesignerRow:
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

class Ice_Tablesets_QueryValueSetItemsDesignerRow:
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

class Ice_Tablesets_QueryWhereItemDesignerRow:
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
      self.UseHaving:bool = obj["UseHaving"]
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

class Ice_Tablesets_QuickSearchBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SvcListRow:
   def __init__(self, obj):
      self.SvcName:str = obj["SvcName"]
      """  ClassName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemCode:str = obj["SystemCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SvcListTableset:
   def __init__(self, obj):
      self.SvcList:list[Ice_Tablesets_SvcListRow] = obj["SvcList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_TableFieldAttributeListRow:
   def __init__(self, obj):
      self.TableID:str = obj["TableID"]
      self.FieldName:str = obj["FieldName"]
      self.AttributeName:str = obj["AttributeName"]
      self.AttributeValue:str = obj["AttributeValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_TableFieldListRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  Database Schema Name  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  Default Value  """  
      self.Required:bool = obj["Required"]
      """  Required  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Read Only  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.External:bool = obj["External"]
      """  External  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.Included:bool = obj["Included"]
      """  Included  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Fiel Name reference  """  
      self.IsNullable:bool = obj["IsNullable"]
      self.CGCCode:str = obj["CGCCode"]
      self.BizType:str = obj["BizType"]
      self.PredictiveSearch:str = obj["PredictiveSearch"]
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      self.CurrencyType:str = obj["CurrencyType"]
      self.CurrencySource:str = obj["CurrencySource"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_TableFieldListTableset:
   def __init__(self, obj):
      self.TableFieldList:list[Ice_Tablesets_TableFieldListRow] = obj["TableFieldList"]
      self.TableFieldAttributeList:list[Ice_Tablesets_TableFieldAttributeListRow] = obj["TableFieldAttributeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtBAQDesignerTableset:
   def __init__(self, obj):
      self.DynamicQueryDesigner:list[Ice_Tablesets_DynamicQueryDesignerRow] = obj["DynamicQueryDesigner"]
      self.QueryCtrlDesigner:list[Ice_Tablesets_QueryCtrlDesignerRow] = obj["QueryCtrlDesigner"]
      self.QueryCtrlValuesDesigner:list[Ice_Tablesets_QueryCtrlValuesDesignerRow] = obj["QueryCtrlValuesDesigner"]
      self.QueryCustomActionDesigner:list[Ice_Tablesets_QueryCustomActionDesignerRow] = obj["QueryCustomActionDesigner"]
      self.QueryExecuteSettingDesigner:list[Ice_Tablesets_QueryExecuteSettingDesignerRow] = obj["QueryExecuteSettingDesigner"]
      self.QueryParameterDesigner:list[Ice_Tablesets_QueryParameterDesignerRow] = obj["QueryParameterDesigner"]
      self.QueryReferenceDesigner:list[Ice_Tablesets_QueryReferenceDesignerRow] = obj["QueryReferenceDesigner"]
      self.QueryParameterBindingDesigner:list[Ice_Tablesets_QueryParameterBindingDesignerRow] = obj["QueryParameterBindingDesigner"]
      self.QuerySubQueryDesigner:list[Ice_Tablesets_QuerySubQueryDesignerRow] = obj["QuerySubQueryDesigner"]
      self.QueryRelationDesigner:list[Ice_Tablesets_QueryRelationDesignerRow] = obj["QueryRelationDesigner"]
      self.QueryRelationFieldDesigner:list[Ice_Tablesets_QueryRelationFieldDesignerRow] = obj["QueryRelationFieldDesigner"]
      self.QuerySortByDesigner:list[Ice_Tablesets_QuerySortByDesignerRow] = obj["QuerySortByDesigner"]
      self.QueryWhereItemDesigner:list[Ice_Tablesets_QueryWhereItemDesignerRow] = obj["QueryWhereItemDesigner"]
      self.QueryGroupByDesigner:list[Ice_Tablesets_QueryGroupByDesignerRow] = obj["QueryGroupByDesigner"]
      self.QueryTableDesigner:list[Ice_Tablesets_QueryTableDesignerRow] = obj["QueryTableDesigner"]
      self.QueryFieldDesigner:list[Ice_Tablesets_QueryFieldDesignerRow] = obj["QueryFieldDesigner"]
      self.QueryFieldAttributeDesigner:list[Ice_Tablesets_QueryFieldAttributeDesignerRow] = obj["QueryFieldAttributeDesigner"]
      self.QueryFunctionCallDesigner:list[Ice_Tablesets_QueryFunctionCallDesignerRow] = obj["QueryFunctionCallDesigner"]
      self.QueryUpdateFieldDesigner:list[Ice_Tablesets_QueryUpdateFieldDesignerRow] = obj["QueryUpdateFieldDesigner"]
      self.QueryUpdateSettingsDesigner:list[Ice_Tablesets_QueryUpdateSettingsDesignerRow] = obj["QueryUpdateSettingsDesigner"]
      self.QueryValueSetItemsDesigner:list[Ice_Tablesets_QueryValueSetItemsDesignerRow] = obj["QueryValueSetItemsDesigner"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UsedInBAQListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  IsGlobal  """  
      self.IsShared:bool = obj["IsShared"]
      """  IsShared  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  GlbCompany  """  
      self.ExtQuery:bool = obj["ExtQuery"]
      """  ExtQuery  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UsedInBAQListTableset:
   def __init__(self, obj):
      self.BAQReportList:list[Ice_Tablesets_BAQReportListRow] = obj["BAQReportList"]
      self.DashBdBAQ:list[Ice_Tablesets_DashBdBAQRow] = obj["DashBdBAQ"]
      self.QuickSearchBAQ:list[Ice_Tablesets_QuickSearchBAQRow] = obj["QuickSearchBAQ"]
      self.UsedInBAQList:list[Ice_Tablesets_UsedInBAQListRow] = obj["UsedInBAQList"]
      self.UsedInReportBAQList:list[Ice_Tablesets_UsedInReportBAQListRow] = obj["UsedInReportBAQList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UsedInReportBAQListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Data Definition Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.Global:bool = obj["Global"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class ImportBaq_input:
   """ Required : 
   newQueryId
   importBytes
   options
   """  
   def __init__(self, obj):
      self.newQueryId:str = obj["newQueryId"]
      self.importBytes:str = obj["importBytes"]
      self.options      #schema had no properties on an object.
      pass

class ImportBaq_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.options: UNKNOW TYPE(error 2338) = obj["options"]
      self.logResult:list = obj[any]
      pass

      """  output parameters  """  

class ImportQuery_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

class ImportQuery_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadKineticQueryDiagram_input:
   """ Required : 
   queryID
   companyID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query(QueryHdr) ID  """  
      self.companyID:str = obj["companyID"]
      """  The Company) ID  """  
      pass

class LoadKineticQueryDiagram_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QueryDiagramTableset] = obj["returnObj"]
      pass

class LoadQueryDiagram_input:
   """ Required : 
   queryID
   companyID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The Query(QueryHdr) ID  """  
      self.companyID:str = obj["companyID"]
      """  The Company) ID  """  
      pass

class LoadQueryDiagram_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QueryDiagramTableset] = obj["returnObj"]
      pass

class PossibleBONames_input:
   """ Required : 
   tableNames
   """  
   def __init__(self, obj):
      self.tableNames:str = obj["tableNames"]
      """  comma delimeted table name list  """  
      pass

class PossibleBONames_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.boNames:str = obj["parameters"]
      pass

      """  output parameters  """  

class RegenUpdatableQueryBpm_input:
   """ Required : 
   companyID
   queryID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.queryID:str = obj["queryID"]
      pass

class RegenUpdatableQueryBpm_output:
   def __init__(self, obj):
      pass

class ResetCache_input:
   """ Required : 
   flags
   """  
   def __init__(self, obj):
      self.flags:int = obj["flags"]
      """  Enumeration of caches to reset  """  
      pass

class ResetCache_output:
   def __init__(self, obj):
      pass

class SaveQueryDiagram_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_QueryDiagramTableset] = obj["ds"]
      pass

class SaveQueryDiagram_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_QueryDiagramTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetSecurityCodeToSystemQuery_input:
   """ Required : 
   queryId
   secCode
   """  
   def __init__(self, obj):
      self.queryId:str = obj["queryId"]
      """  Id of system query  """  
      self.secCode:str = obj["secCode"]
      """  Security code  """  
      pass

class SetSecurityCodeToSystemQuery_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQDesignerTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQDesignerTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateQueriesSecurityFiltersByDs_input:
   """ Required : 
   extDsName
   extDsTypeName
   """  
   def __init__(self, obj):
      self.extDsName:str = obj["extDsName"]
      """  ID of External Datasource or empty string if next param value is specified  """  
      self.extDsTypeName:str = obj["extDsTypeName"]
      """  ID of External Datasource Type or empty string if first param value specified  """  
      pass

class UpdateQueriesSecurityFiltersByDs_output:
   def __init__(self, obj):
      pass

class UpdateQuerySecurityFilters_input:
   """ Required : 
   queryTableSet
   """  
   def __init__(self, obj):
      self.queryTableSet:list[Ice_Tablesets_BAQDesignerTableset] = obj["queryTableSet"]
      pass

class UpdateQuerySecurityFilters_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQDesignerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateQueryID_input:
   """ Required : 
   queryID
   companyID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The proposed Query ID  """  
      self.companyID:str = obj["companyID"]
      """  The company where to search query  """  
      pass

class ValidateQueryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.foundQueryID:str = obj["parameters"]
      self.foundCompanyID:str = obj["parameters"]
      self.authorID:str = obj["parameters"]
      self.isShared:bool = obj["isShared"]
      self.isExternal:bool = obj["isExternal"]
      self.isSystem:bool = obj["isSystem"]
      self.isGlobal:bool = obj["isGlobal"]
      self.secCode:str = obj["parameters"]
      pass

      """  output parameters  """  

