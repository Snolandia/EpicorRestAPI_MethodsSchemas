import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MobileEmpExpenseSvc
# Description: Mobile Employee Expense Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileEmpExpenses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileEmpExpenses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses",headers=creds) as resp:
           return await resp.json()

async def post_MobileEmpExpenses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileEmpExpenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum(Company, EmpID, EmpExpenseNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileEmpExpense item
   Description: Calls GetByID to retrieve the MobileEmpExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileEmpExpenses_Company_EmpID_EmpExpenseNum(Company, EmpID, EmpExpenseNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileEmpExpense for the service
   Description: Calls UpdateExt to update MobileEmpExpense. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileEmpExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileEmpExpenses_Company_EmpID_EmpExpenseNum(Company, EmpID, EmpExpenseNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileEmpExpense item
   Description: Call UpdateExt to delete MobileEmpExpense item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileEmpExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseComments(Company, EmpID, EmpExpenseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MobileEmpExpenseComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileEmpExpenseComments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseComments",headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseComment item
   Description: Calls GetByID to retrieve the MobileEmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseComment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseAttches(Company, EmpID, EmpExpenseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MobileEmpExpenseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileEmpExpenseAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseAttches",headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseAttch item
   Description: Calls GetByID to retrieve the MobileEmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenseComments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileEmpExpenseComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileEmpExpenseComments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments",headers=creds) as resp:
           return await resp.json()

async def post_MobileEmpExpenseComments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileEmpExpenseComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseComment item
   Description: Calls GetByID to retrieve the MobileEmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileEmpExpenseComment for the service
   Description: Calls UpdateExt to update MobileEmpExpenseComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileEmpExpenseComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileEmpExpenseComment item
   Description: Call UpdateExt to delete MobileEmpExpenseComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileEmpExpenseComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenseAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileEmpExpenseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileEmpExpenseAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches",headers=creds) as resp:
           return await resp.json()

async def post_MobileEmpExpenseAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileEmpExpenseAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseAttch item
   Description: Calls GetByID to retrieve the MobileEmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileEmpExpenseAttch for the service
   Description: Calls UpdateExt to update MobileEmpExpenseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileEmpExpenseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileEmpExpenseAttch item
   Description: Call UpdateExt to delete MobileEmpExpenseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileEmpExpenseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileApproverLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileApproverLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileApproverLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileApproverListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists",headers=creds) as resp:
           return await resp.json()

async def post_MobileApproverLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileApproverLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileApproverLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileApproverList item
   Description: Calls GetByID to retrieve the MobileApproverList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileApproverList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileApproverLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileApproverList for the service
   Description: Calls UpdateExt to update MobileApproverList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileApproverList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileApproverLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileApproverList item
   Description: Call UpdateExt to delete MobileApproverList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileApproverList
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMobileEmpExpense, whereClauseMobileEmpExpenseAttch, whereClauseMobileEmpExpenseComment, whereClauseMobileApproverList, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseMobileEmpExpense=" + whereClauseMobileEmpExpense
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileEmpExpenseAttch=" + whereClauseMobileEmpExpenseAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileEmpExpenseComment=" + whereClauseMobileEmpExpenseComment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileApproverList=" + whereClauseMobileApproverList
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(empID, empExpenseNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
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
   params += "empID=" + empID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "empExpenseNum=" + empExpenseNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetMobileEmpExpenseAttchs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMobileEmpExpenseAttchs
   Description: Custom Method to retrieve only the MobileEmpExpenseAttch records for the current expense
   OperationID: GetMobileEmpExpenseAttchs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMobileEmpExpenseAttchs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileEmpExpenseAttchs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMobileEmpExpenseComments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMobileEmpExpenseComments
   Description: Custom Method to retrieve only the MobileEmpExpenseComment records for the current expense
   OperationID: GetMobileEmpExpenseComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMobileEmpExpenseComments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileEmpExpenseComments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetApprovalStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetApprovalStatus
   Description: Populates the MobileApproverList Temp Table with the current expense's approver data.
   OperationID: MobileGetApprovalStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetApprovalStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetApprovalStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetByID
   Description: GetByID method
   OperationID: MobileGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetRows
   Description: Returns MobileEmpExpense dataset containing all rows that satisfy the where clauses
   OperationID: MobileGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetRowsApprover(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetRowsApprover
   Description: Retrieves all approver expenses to be approved / rejected / recalled from approval.
   OperationID: MobileGetRowsApprover
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRowsApprover_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsApprover_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetList
   Description: Get List method
   OperationID: MobileGetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHomePageData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHomePageData
   OperationID: GetHomePageData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHomePageData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHomePageData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewEmpExpense
   Description: Create a new mobile EmpExpense dataset row
   OperationID: MobileGetNewEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewEmpExpenseAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewEmpExpenseAttch
   Description: Create a new mobile EmpExpense dataset attachment row
   OperationID: MobileGetNewEmpExpenseAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewEmpExpenseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewEmpExpenseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewEmpExpenseComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewEmpExpenseComment
   Description: Create a new mobile EmpExpense dataset comment row
   OperationID: MobileGetNewEmpExpenseComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewEmpExpenseComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewEmpExpenseComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDelete
   Description: Method to call to delete expense records
   OperationID: MobileDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileSync(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileSync
   Description: Method to call to synchronize draft records to the database
   OperationID: MobileSync
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileSync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSync_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileSyncSuccessful(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileSyncSuccessful
   Description: Receives the fields needed to find and delete the validation record created when synchronization is successful
   OperationID: MobileSyncSuccessful
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileSyncSuccessful_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSyncSuccessful_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileAttachmentUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileAttachmentUpdate
   Description: Method to call to update attachment record and upload file to the storage defined by document type (or default company storage)
   OperationID: MobileAttachmentUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileAttachmentUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileAttachmentUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileUpdate
   Description: Method to call to update the table set
   OperationID: MobileUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RecallEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallEmpExpense
   Description: Method to call when recalling submitted expense records
   OperationID: RecallEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SubmitSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitSelected
   Description: Method to call to submit selected expenses
   OperationID: SubmitSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRecallFromApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRecallFromApproval
   Description: The procedure is called prior to performing a recall.  It will check
if subsequent approvals have occurred.  If they have the user
will have the opportunity to cancel the recall.
   OperationID: CheckRecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallFromApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallFromApproval
   Description: Method to call when recalling from approval entry
   OperationID: RecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveReject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveReject
   Description: The procedure is called when the user selects EmpExpense records for reject or approve
   OperationID: ApproveReject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyEmpExpense
   Description: Method to copy the vales from one EmpExpense record to a new EmpExpense record.
   OperationID: CopyEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMobileEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMobileEmpExpense
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMobileEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMobileEmpExpenseAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMobileEmpExpenseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileEmpExpenseAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMobileEmpExpenseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileEmpExpenseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMobileEmpExpenseComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMobileEmpExpenseComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileEmpExpenseComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMobileEmpExpenseComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileEmpExpenseComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileApproverListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileEmpExpenseAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseCommentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileEmpExpenseCommentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileEmpExpenseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileEmpExpenseRow] = obj["value"]
      pass

class Erp_Tablesets_MobileApproverListRow:
   def __init__(self, obj):
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """  The status of the current approval task.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  Date when the approval task was completed.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  """  
      self.Key2:str = obj["Key2"]
      """  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name corresponding to the SalesRepCode.  """  
      self.SequenceNum:int = obj["SequenceNum"]
      """  Number used to display the records in their correct sequence in the mobile app.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense comment record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseTaxAmt:int = obj["DocExpenseTaxAmt"]
      """  The tax of the expense in the expense currency.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.DocTotalExpenseAmt:int = obj["DocTotalExpenseAmt"]
      """  The total amount of the expense in the expense currency.  This value includes taxes.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Expense Comment  """  
      self.ExpCommentInstr:str = obj["ExpCommentInstr"]
      """  Expense Comment Instruction  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayStatus:str = obj["DisplayStatus"]
      """  External field to display a descriptive status of the record  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available in approval entry  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.ExpenseDisableDelete:bool = obj["ExpenseDisableDelete"]
      self.ExpenseDisableUpdate:bool = obj["ExpenseDisableUpdate"]
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the expense detail has attachments  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the expense detail has comments  """  
      self.EnableUnitRate:bool = obj["EnableUnitRate"]
      """  Indicates if UnitRate is enabled  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  MobileGetApprovalStatus  """  
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      """  A list of people who need to approve the expense.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpCurrencyCurrSymbol:str = obj["ExpCurrencyCurrSymbol"]
      self.ExpCurrencyDocumentDesc:str = obj["ExpCurrencyDocumentDesc"]
      self.ExpCurrencyCurrName:str = obj["ExpCurrencyCurrName"]
      self.ExpCurrencyCurrDesc:str = obj["ExpCurrencyCurrDesc"]
      self.ExpCurrencyCurrencyID:str = obj["ExpCurrencyCurrencyID"]
      self.PayMethodReimbursable:bool = obj["PayMethodReimbursable"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscExpUnitBased:bool = obj["PurMiscExpUnitBased"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ApproveReject_input:
   """ Required : 
   salesRepCode
   action
   comment
   ds
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.action:str = obj["action"]
      """  Action to take A = approver, R = reject.  """  
      self.comment:str = obj["comment"]
      """  Comment text if comments are to be created.  """  
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class ApproveReject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRecallFromApproval_input:
   """ Required : 
   salesRepCode
   ds
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class CheckRecallFromApproval_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.outRecallMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyEmpExpense_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class CopyEmpExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MobileApproverListRow:
   def __init__(self, obj):
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """  The status of the current approval task.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  Date when the approval task was completed.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  """  
      self.Key2:str = obj["Key2"]
      """  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name corresponding to the SalesRepCode.  """  
      self.SequenceNum:int = obj["SequenceNum"]
      """  Number used to display the records in their correct sequence in the mobile app.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense comment record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseTaxAmt:int = obj["DocExpenseTaxAmt"]
      """  The tax of the expense in the expense currency.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseListTableset:
   def __init__(self, obj):
      self.MobileEmpExpenseList:list[Erp_Tablesets_MobileEmpExpenseListRow] = obj["MobileEmpExpenseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MobileEmpExpenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.DocTotalExpenseAmt:int = obj["DocTotalExpenseAmt"]
      """  The total amount of the expense in the expense currency.  This value includes taxes.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Expense Comment  """  
      self.ExpCommentInstr:str = obj["ExpCommentInstr"]
      """  Expense Comment Instruction  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayStatus:str = obj["DisplayStatus"]
      """  External field to display a descriptive status of the record  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available in approval entry  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.ExpenseDisableDelete:bool = obj["ExpenseDisableDelete"]
      self.ExpenseDisableUpdate:bool = obj["ExpenseDisableUpdate"]
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the expense detail has attachments  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the expense detail has comments  """  
      self.EnableUnitRate:bool = obj["EnableUnitRate"]
      """  Indicates if UnitRate is enabled  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  MobileGetApprovalStatus  """  
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      """  A list of people who need to approve the expense.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpCurrencyCurrSymbol:str = obj["ExpCurrencyCurrSymbol"]
      self.ExpCurrencyDocumentDesc:str = obj["ExpCurrencyDocumentDesc"]
      self.ExpCurrencyCurrName:str = obj["ExpCurrencyCurrName"]
      self.ExpCurrencyCurrDesc:str = obj["ExpCurrencyCurrDesc"]
      self.ExpCurrencyCurrencyID:str = obj["ExpCurrencyCurrencyID"]
      self.PayMethodReimbursable:bool = obj["PayMethodReimbursable"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscExpUnitBased:bool = obj["PurMiscExpUnitBased"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileEmpExpenseTableset:
   def __init__(self, obj):
      self.MobileEmpExpense:list[Erp_Tablesets_MobileEmpExpenseRow] = obj["MobileEmpExpense"]
      self.MobileEmpExpenseAttch:list[Erp_Tablesets_MobileEmpExpenseAttchRow] = obj["MobileEmpExpenseAttch"]
      self.MobileEmpExpenseComment:list[Erp_Tablesets_MobileEmpExpenseCommentRow] = obj["MobileEmpExpenseComment"]
      self.MobileApproverList:list[Erp_Tablesets_MobileApproverListRow] = obj["MobileApproverList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMobileEmpExpenseTableset:
   def __init__(self, obj):
      self.MobileEmpExpense:list[Erp_Tablesets_MobileEmpExpenseRow] = obj["MobileEmpExpense"]
      self.MobileEmpExpenseAttch:list[Erp_Tablesets_MobileEmpExpenseAttchRow] = obj["MobileEmpExpenseAttch"]
      self.MobileEmpExpenseComment:list[Erp_Tablesets_MobileEmpExpenseCommentRow] = obj["MobileEmpExpenseComment"]
      self.MobileApproverList:list[Erp_Tablesets_MobileApproverListRow] = obj["MobileApproverList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

class GetHomePageData_input:
   """ Required : 
   employeeID
   salesRepCode
   numberOfDays
   """  
   def __init__(self, obj):
      self.employeeID:str = obj["employeeID"]
      self.salesRepCode:str = obj["salesRepCode"]
      self.numberOfDays:int = obj["numberOfDays"]
      pass

class GetHomePageData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.entered:int = obj["parameters"]
      self.submitted:int = obj["parameters"]
      self.approved:int = obj["parameters"]
      self.rejected:int = obj["parameters"]
      self.forApproval:int = obj["parameters"]
      self.oldestRecordDate:str = obj["parameters"]
      self.submittedTotal:int = obj["parameters"]
      self.enteredTotal:int = obj["parameters"]
      self.approvedTotal:int = obj["parameters"]
      self.rejectedTotal:int = obj["parameters"]
      self.forApprovalTotal:int = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMobileEmpExpenseAttchs_input:
   """ Required : 
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      self.empExpenseNum:int = obj["empExpenseNum"]
      """  Expense Number  """  
      pass

class GetMobileEmpExpenseAttchs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

class GetMobileEmpExpenseComments_input:
   """ Required : 
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      self.empExpenseNum:int = obj["empExpenseNum"]
      """  Expense Number  """  
      pass

class GetMobileEmpExpenseComments_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

class GetNewMobileEmpExpenseAttch_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class GetNewMobileEmpExpenseAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMobileEmpExpenseComment_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class GetNewMobileEmpExpenseComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMobileEmpExpense_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      pass

class GetNewMobileEmpExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMobileEmpExpense
   whereClauseMobileEmpExpenseAttch
   whereClauseMobileEmpExpenseComment
   whereClauseMobileApproverList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMobileEmpExpense:str = obj["whereClauseMobileEmpExpense"]
      self.whereClauseMobileEmpExpenseAttch:str = obj["whereClauseMobileEmpExpenseAttch"]
      self.whereClauseMobileEmpExpenseComment:str = obj["whereClauseMobileEmpExpenseComment"]
      self.whereClauseMobileApproverList:str = obj["whereClauseMobileApproverList"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVersion_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

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

class MobileAttachmentUpdate_input:
   """ Required : 
   ds
   docTypeID
   parentTable
   fileName
   data
   metadata
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.docTypeID:str = obj["docTypeID"]
      """  Document Type ID  """  
      self.parentTable:str = obj["parentTable"]
      """  Parent Table e.g. LaborDtl  """  
      self.fileName:str = obj["fileName"]
      """  Physical name of the file  """  
      self.data:str = obj["data"]
      """  Array of bytes representing the data of the attachment  """  
      self.metadata      #schema had no properties on an object.
      """  Metadata  """  
      pass

class MobileAttachmentUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileDelete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class MobileDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetApprovalStatus_input:
   """ Required : 
   key1
   key2
   approvedBy
   pendingApprovalBy
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.approvedBy:str = obj["approvedBy"]
      self.pendingApprovalBy:str = obj["pendingApprovalBy"]
      pass

class MobileGetApprovalStatus_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

class MobileGetByID_input:
   """ Required : 
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class MobileGetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

class MobileGetList_input:
   """ Required : 
   mobileEmpExpenseWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.mobileEmpExpenseWhereClause:str = obj["mobileEmpExpenseWhereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class MobileGetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileGetNewEmpExpenseAttch_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      """  The employee id  """  
      self.empExpenseNum:int = obj["empExpenseNum"]
      """  The expense number  """  
      pass

class MobileGetNewEmpExpenseAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewEmpExpenseComment_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      """  The employee id  """  
      self.empExpenseNum:int = obj["empExpenseNum"]
      """  The expense number  """  
      pass

class MobileGetNewEmpExpenseComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewEmpExpense_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      """  The employee id  """  
      pass

class MobileGetNewEmpExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetRowsApprover_input:
   """ Required : 
   salesRepCode
   empID
   expenseDateFrom
   expenseDateTo
   expenseStatuses
   expenseTypes
   amountMinimum
   amountMaximum
   groupBy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      self.empID:str = obj["empID"]
      self.expenseDateFrom:str = obj["expenseDateFrom"]
      self.expenseDateTo:str = obj["expenseDateTo"]
      self.expenseStatuses:str = obj["expenseStatuses"]
      self.expenseTypes:str = obj["expenseTypes"]
      self.amountMinimum:int = obj["amountMinimum"]
      self.amountMaximum:int = obj["amountMaximum"]
      self.groupBy:str = obj["groupBy"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class MobileGetRowsApprover_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileGetRows_input:
   """ Required : 
   whereClauseMobileEmpExpense
   whereClauseMobileEmpExpenseAttch
   whereClauseMobileEmpExpenseComment
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMobileEmpExpense:str = obj["whereClauseMobileEmpExpense"]
      self.whereClauseMobileEmpExpenseAttch:str = obj["whereClauseMobileEmpExpenseAttch"]
      self.whereClauseMobileEmpExpenseComment:str = obj["whereClauseMobileEmpExpenseComment"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class MobileGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileSyncSuccessful_input:
   """ Required : 
   company
   tableName
   sysRowID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company where the record was created  """  
      self.tableName:str = obj["tableName"]
      """  Name of the table related to the patch field  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID of the record on the Mobile  """  
      pass

class MobileSyncSuccessful_output:
   def __init__(self, obj):
      pass

class MobileSync_input:
   """ Required : 
   tableName
   ds
   comments
   salesRepCode
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Name of the table that is being synchronized.  """  
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.comments:str = obj["comments"]
      """  Comments for approved and rejected records  """  
      self.salesRepCode:str = obj["salesRepCode"]
      """  Sales Rep Code  """  
      pass

class MobileSync_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class MobileUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecallEmpExpense_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class RecallEmpExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecallFromApproval_input:
   """ Required : 
   salesRepCode
   ds
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class RecallFromApproval_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SubmitSelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class SubmitSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMobileEmpExpenseTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMobileEmpExpenseTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileEmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

